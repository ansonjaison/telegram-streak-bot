"""
Telegram Streak Bot

A motivational Telegram bot that tracks user streaks based on message activity in a group.
- Rewards daily messaging with increased streaks
- Sends inactivity warnings
- Displays top streak holders
- Keeps itself alive via Flask + Replit pinging
"""

import json
import os
import random
from datetime import datetime, timedelta
import pytz
from flask import Flask
from threading import Thread, Lock
import asyncio
import nest_asyncio
import time
import requests
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          ContextTypes, filters)
from apscheduler.schedulers.background import BackgroundScheduler

# === BOT SETTINGS ===

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # <-- Replace this with your bot token
GROUP_ID = -1234567890  # <-- Replace this with your target group ID (negative for supergroups)
DATA_FILE = "user_data.json"  # Ensure this file exists with empty `{}` if running for the first time
IST = pytz.timezone("Asia/Kolkata")

# === MESSAGES ===

GREETINGS = [
    "🌞 Good morning, {mention}! Keep it going! 🔥 Your streak is now {streak}!",
    "👊 You're back, {mention}! That's how champions roll. Streak: {streak}! 😎",
    "✨ Great to see you again, {mention}! Updated your streak to {streak} 🔥",
    "🚀 {mention}, you're on fire! Your streak is now {streak} 🔥🔥🔥"
]

WARNING_MESSAGES = [
    "⚠️ {mention}, you've been inactive for over 24 hours! Message now or lose your streak!",
    "👀 {mention}, still waiting for your message! Don't let your streak die!"
]

lock = Lock()


# === JSON Utilities ===

def load_data():
    """Load streak data from the JSON file. If file is missing, return empty dict."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    """Save streak data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


# === Command Handlers ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts a new streak or displays current streak if already started."""
    user = update.effective_user
    if not user:
        return

    with lock:
        data = load_data()
        uid = str(user.id)
        now = datetime.now(IST)

        if uid not in data:
            data[uid] = {
                "name": user.first_name,
                "last_message": now.isoformat(),
                "streak": 1
            }
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            msg = f"👋 Welcome, {mention}! Your streak starts now!"
        else:
            streak = data[uid]["streak"]
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            msg = f"🔥 Hey {mention}, your current streak is {streak} days!"

        save_data(data)

    await update.message.reply_text(msg, parse_mode="Markdown")


async def streak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays the user's current streak."""
    user = update.effective_user
    if not user:
        return

    with lock:
        data = load_data()
        uid = str(user.id)
        streak = data.get(uid, {}).get("streak", 0)

    await update.message.reply_text(f"🔥 Your current streak is {streak} days!")


async def show_top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays top 5 users with highest streaks."""
    with lock:
        data = load_data()
        leaderboard = sorted(data.items(),
                             key=lambda x: x[1]["streak"],
                             reverse=True)
        top5 = leaderboard[:5]

        if not top5:
            msg = "No streaks yet. Be the first to start!"
        else:
            msg = "🏆 *Top 5 Streaks:*\n\n"
            for i, (uid, entry) in enumerate(top5, start=1):
                mention = f"[{entry['name']}](tg://user?id={uid})"
                msg += f"{i}. {mention} — {entry['streak']} 🔥\n"

    await update.message.reply_markdown(msg)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows available bot commands."""
    await update.message.reply_text(
        "🤖 *Streak Bot Commands:*\n"
        "/start – Start your streak journey\n"
        "/streak – View your current streak\n"
        "/top – View top streak holders\n"
        "/help – Show this message",
        parse_mode="Markdown")


# === Message Handler (Streak Logic) ===

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tracks user messages and updates streak based on activity."""
    user = update.effective_user
    if not user or not update.message:
        return

    with lock:
        data = load_data()
        uid = str(user.id)
        now = datetime.now(IST)

        if uid not in data:
            # First time user
            data[uid] = {
                "name": user.first_name,
                "last_message": now.isoformat(),
                "streak": 1
            }
            msg = f"👋 Hi {user.first_name}, your streak starts now! 🔥"
        else:
            last = datetime.fromisoformat(data[uid]["last_message"])
            diff = (now.date() - last.date()).days

            if diff == 1:
                data[uid]["streak"] += 1
                mention = f"[{user.first_name}](tg://user?id={user.id})"
                msg = random.choice(GREETINGS).format(
                    mention=mention, streak=data[uid]["streak"])
            elif diff > 1:
                data[uid]["streak"] = 1
                msg = f"😓 Oops, {user.first_name}, you missed {diff} days. Starting over at 1."
            else:
                return  # Already updated today

            data[uid]["last_message"] = now.isoformat()

        save_data(data)

    await update.message.reply_text(msg, parse_mode="Markdown")


# === Inactivity Warning Job ===

async def check_inactivity(app):
    """Sends warning messages in the group for inactive users."""
    with lock:
        data = load_data()
        now = datetime.now(IST)

        for uid, entry in data.items():
            last_msg = datetime.fromisoformat(entry["last_message"])
            if (now - last_msg) > timedelta(hours=24):
                try:
                    mention = f"[{entry['name']}](tg://user?id={uid})"
                    msg = random.choice(WARNING_MESSAGES).format(mention=mention)
                    await app.bot.send_message(chat_id=GROUP_ID, text=msg, parse_mode="Markdown")
                except Exception as e:
                    print(f"Failed to warn {uid}: {e}")


# === Flask server for keep-alive ===

def run_flask():
    """Starts a Flask server to keep the bot alive on Replit."""
    app = Flask(__name__)

    @app.route('/')
    def home():
        try:
            with open("status.html", "r") as file:
                return file.read()
        except Exception as e:
            return f"<h1>Error loading status page</h1><p>{e}</p>"

    app.run(host='0.0.0.0', port=8080)


# === Background Scheduler ===

def start_scheduler(app):
    """Starts a background job to check for inactive users every 6 hours."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: asyncio.create_task(check_inactivity(app)), 'interval', hours=6)
    scheduler.start()


# === Ping for Replit Keep-alive ===

def keep_alive():
    """Pings the Flask server every 10 minutes to prevent sleeping."""
    def ping():
        while True:
            try:
                print("🔁 Pinging to keep alive...")
                requests.get("https://your-replit-app-url.repl.co/")  # <-- Replace with your Replit URL
            except Exception as e:
                print(f"Ping failed: {e}")
            time.sleep(600)

    thread = Thread(target=ping)
    thread.daemon = True
    thread.start()


# === Main Entrypoint ===

async def main():
    """Main bot entrypoint — registers commands, starts Flask and scheduler."""
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("streak", streak))
    app.add_handler(CommandHandler("top", show_top))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    start_scheduler(app)

    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    keep_alive()

    print("🤖 Bot is running... Waiting for messages.")
    await app.run_polling()


if __name__ == '__main__':
    nest_asyncio.apply()
    asyncio.run(main())
