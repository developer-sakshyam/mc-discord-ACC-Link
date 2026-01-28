🔗 MC-Discord-Link
Open-Source Minecraft ↔ Discord Account & Rank Sync
<p align="center"> <b>Link accounts once. Sync ranks automatically.</b><br> A free and open-source system to link Minecraft accounts with Discord<br> and automatically assign Discord roles based on in-game ranks. </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Discord.py-2.x-5865F2?logo=discord&logoColor=white"> <img src="https://img.shields.io/badge/Minecraft-Paper%20%7C%20Spigot-green"> <img src="https://img.shields.io/badge/Database-SQLite%20%7C%20MySQL-blue"> <img src="https://img.shields.io/github/license/your-username/mc-discord-link"> </p>
🌍 About

MC-Discord-Link is a lightweight system that connects a player’s Minecraft account to their Discord account and keeps their ranks in sync.

Once linked:

Discord roles are assigned automatically

Staff don’t need to manage roles manually

Rank verification becomes fast and reliable

This project is 100% free, open-source, and designed to work with any Minecraft server.

⚙️ How It Works (Simple Version)

Player runs a command in Minecraft → receives a link code

Player runs /link <code> in Discord

Bot verifies the code using the database

Minecraft UUID ↔ Discord ID is stored

Discord role is assigned based on the player’s in-game rank

That’s it.
No web panel. No bloated dependencies.

🧩 Features

✅ Minecraft ↔ Discord account linking
✅ Automatic Discord role assignment
✅ Supports LuckPerms ranks
✅ SQLite support (local testing)
✅ MySQL / MariaDB support (production)
✅ Works across different hostings
✅ Fully open-source & customizable

📁 Project Structure
mc-discord-link/
├── discord-bot/
│   ├── bot.py
│   ├── database.py
│   ├── config.py
│   └── requirements.txt
│
├── minecraft-plugin/
│   ├── src/
│   └── plugin.yml
│
└── link.db   # SQLite (local only)

🗃️ Database Configuration
🟢 SQLite (Default – Local Use)

By default, the system uses SQLite:

DB_PATH = "/path/to/link.db"


✅ Easy setup
❌ Bot and Minecraft server must be on the same machine

🔵 MySQL / MariaDB (Recommended)

If your Discord bot and Minecraft server are hosted separately, you must use MySQL or MariaDB.

Replace SQLite with:

DB_CONFIG = {
    "host": "DB_HOST",
    "user": "DB_USER",
    "password": "DB_PASSWORD",
    "database": "DB_NAME",
    "port": 3306
}


Both the bot and the plugin must use the same database.

🤖 Discord Bot Setup

Create a bot in Discord Developer Portal

Enable:

Server Members Intent

Message Content Intent

Invite the bot with:

Manage Roles

Install dependencies:

pip install -r requirements.txt


Start the bot:

python bot.py


⚠️ Important:
The bot’s role must be higher than the roles it assigns.

⛏️ Minecraft Plugin Setup

Build or download the plugin JAR

Put it inside:

/plugins


Configure the database

Restart the server

🚨 Common Issues
❌ 403 Forbidden: Missing Permissions

Bot role is below the target role

Bot lacks Manage Roles

❌ Linking fails

Bot and plugin using different databases

Wrong DB credentials

❌ SQLite not syncing

Bot and server are on different machines (expected)

🧠 Customization

You can:

Map ranks to custom Discord roles

Extend commands

Add logging

Switch databases anytime

The code is intentionally kept simple so servers can modify it easily.

📜 License

MIT License
Free to use, modify, and distribute.
