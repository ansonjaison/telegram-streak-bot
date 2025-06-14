# 🤖 Mr Manager Bot

> Telegram Bot: [Mr Manager](https://t.me/Sergio_R0bot)  
> Developed by: [Anson Jaison](https://in.linkedin.com/in/anson-jaison)  
> Contact: i_anson@outlook.in | [X (Twitter)](https://twitter.com/i_ansonjaison)

---

## 📌 What is Mr Manager?

**Mr Manager** is a personalized Telegram bot built to help manage group activities more efficiently with automation and tracking features. Whether you're managing group members, events, or reminders, Mr Manager acts like your group's intelligent assistant.  

Designed for small communities or close-knit circles, it’s lightweight, customizable, and runs entirely from a single Python file!

---
## ✨ Key Features of Mr Manager Bot

Track user activity, reward consistency, and keep your group lively — all on autopilot!

### 🔥 Streak System
- ✅ **Daily Streak Tracking**: Automatically tracks daily streaks for each active group member.
- 📆 **Midnight Auto-Update**: Updates streaks daily at midnight — no manual triggers needed.
- ⚠️ **Missed Day Warnings**: Warns users who miss a day (logic can be customized).
- 🧨 **Streak Reset Logic**: Resets a user's streak after missing two consecutive days (configurable).
- 🏆 **Leaderboard**: Displays top streak holders on command.
- 📈 **Personal Stats**: Users can view their own current streak anytime.

### 🧠 Smart Features
- ⏳ **Grace Period Logic**: Prevents unfair penalties during low activity or early setup.
- 🚫 **Anti-Spam Friendly**: Counts only one message per user per day — no spamming to climb the leaderboard.
- 👥 **Supports Multiple Users**: Scales to track streaks across large groups.

### 🌐 Hosting & Status
- 🖥️ **Uptime Page**: Comes with a simple `status.html` page to confirm the bot is alive — perfect for hosting on platforms like Replit, Railway, or Render.
- 💡 **Single-File Simplicity**: Runs everything from a single Python file (`main.py`) with no external databases.
- 📁 **Local Data Storage**: Saves user streak data to a lightweight `.json` file.

---

> 🎯 Ideal for:  
> Habit-tracking groups, daily stand-ups, productivity challenges, language learning streaks, or just some fun community competition.

---

## 📁 Project Structure

```
telegram-streak-bot/
├── main.py            # Main bot code (everything in one place)
├── status.html        # Simple status page shown on web (for uptime checks)
├── user_data.json     # (REQUIRED) Empty file created by user manually
├── requirements.txt   # Python dependencies
├── .gitignore         # To avoid uploading runtime/cache files
├── README.md          # You’re reading it
├── LICENSE            # Open source license (MIT)
```

> ⚠️ **Important:**  
> Before you run the bot, you must manually create a file named `user_data.json` in the root folder.  
> It should be an **empty JSON object** like this:
> ```json
> {}
> ```

---

## 🚀 How it Works

1. **Create a bot** on [@BotFather](https://t.me/BotFather) and get your token.
2. **Paste your bot token** into the `main.py` where required.
3. **Run the script** (you can use Replit or your local machine).
4. Your bot will start responding to commands in your Telegram group.
5. Data will be saved inside the `user_data.json` file during runtime.

---

## 🔧 Deployment (e.g., Replit)

- Just create a Replit project and upload your `main.py`.
- Add `requirements.txt` so Replit installs dependencies automatically.
- Use something like [UptimeRobot](https://uptimerobot.com) to ping your Replit URL and keep it alive.

> *No special server is needed — everything works from a single file.*

---

## 📦 Installation (for local setup)

```bash
# Clone the repo (or copy files)
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create user_data.json with an empty object:
echo "{}" > user_data.json

# Run the bot
python main.py
```

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Developed by **[Anson Jaison](https://in.linkedin.com/in/anson-jaison)**  
📩 Contact: i_anson@outlook.in  
🐦 Twitter: [@i_ansonjaison](https://twitter.com/i_ansonjaison)  

> Special thanks to **ChatGPT by OpenAI** for code structuring, deployment help, and README generation.

---

## 💬 Need Help?

If you run into any issues with deployment or setup, feel free to reach out on [LinkedIn](https://in.linkedin.com/in/anson-jaison) or [X (Twitter)](https://twitter.com/i_ansonjaison). I’d be happy to help!
