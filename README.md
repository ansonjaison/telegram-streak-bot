# 🤖 Mr Manager — Telegram Group Assistant Bot

> A lightweight, always-available Telegram bot built for personal group management and fun interactions.  
> Developed with ❤️ by Anson Jaison, with guidance from ChatGPT.

---

## 📌 What is Mr Manager?

**Mr Manager** is a custom Telegram bot built to assist with managing a private Telegram group — responding to simple commands, giving updates, and staying reliably online using free deployment tools. It’s minimal, easy to set up, and perfect for running within small private communities or groups.

**Bot Link**: [@Sergio_R0bot](https://t.me/Sergio_R0bot)

---

## ✨ Features

- ✅ Replies to basic group messages or commands like `/start`, `/help`, or custom responses
- ⚙️ Easily editable to add your own triggers and replies
- 🌐 Runs on free cloud using [Replit](https://replit.com/)
- 🔄 Stays alive with uptime monitoring via [UptimeRobot](https://uptimerobot.com/)
- 🔐 Fully customizable with your own token from [@BotFather](https://t.me/BotFather)
- 🚀 Ideal for private Telegram groups

---

## 🧠 How It Works (Simple)

1. You create a bot with **@BotFather** on Telegram
2. You get an API token
3. You paste the code into Replit, insert your token
4. A small Flask server responds to pings to keep it alive
5. You monitor it with **UptimeRobot** so the bot stays up 24/7 (or revive manually)

---

## 🛠️ Full Setup Guide

### 🔸 Step 1: Create the Bot on Telegram

1. Go to [@BotFather](https://t.me/BotFather)
2. Type `/start`
3. Type `/newbot` and follow instructions:
   - Choose a display name (e.g., `Mr Manager`)
   - Choose a username (must end with `bot`, e.g., `Sergio_R0bot`)
4. You’ll receive a **Bot Token**, like:

   ```
   123456789:ABCDefGhiJKlmNopQRStuvWXYz12345678
   ```

---

### 🔸 Step 2: Deploy the Bot

- Paste the provided code in a Python-based Replit project.
- Replace your bot token where needed.
- Make sure the Flask app runs to serve a route like `/` for uptime checks.
- Once launched, it’ll start replying instantly in Telegram.

---

### 🔸 Step 3: Keep It Alive Using UptimeRobot

1. Go to [https://uptimerobot.com/](https://uptimerobot.com/)
2. Sign up for a free account
3. Click **"Add New Monitor"**
   - **Monitor Type**: HTTP(s)
   - **Friendly Name**: Mr Manager Bot
   - **URL**: Your Replit web URL (e.g., `https://your-repl-name.replit.app/`)
   - **Monitoring Interval**: 5 minutes
4. Add your email/alert method

This helps you keep your bot online all the time.

---

## 🧪 Using the Bot

1. Open Telegram and message the bot directly or in your group
2. Try `/start`, `/help`, or send a message — the bot responds
3. Works perfectly for private management or simple fun interactions

---

## 👨‍💻 Developed By

**Anson Jaison**  
📧 Email: [i_anson@outlook.in](mailto:i_anson@outlook.in)  
🔗 [LinkedIn](https://in.linkedin.com/in/anson-jaison)  
🐦 [X (Twitter)](https://twitter.com/i_ansonjaison)

> Built with love and minimal code, this project was made possible with the help of **ChatGPT** — providing technical guidance, structure, and code suggestions every step of the way.

---

## 💬 Need Help?

If you run into **any issues** while deploying or maintaining the bot, feel free to reach out.  
📬 Preferably message me on [LinkedIn](https://in.linkedin.com/in/anson-jaison) or [X](https://twitter.com/i_ansonjaison).

---

## 🙌 Final Note

Mr Manager is a lean, personal, and effective solution for group management — without bloat, without complexity.  
Just a small Telegram bot doing its job — quietly and reliably.

Enjoy the experience 💡
