<!-- ===================================== -->
<!-- 🔗 MC ↔ DISCORD LINK & RANK SYNC -->
<!-- ===================================== -->

<h1 align="center">🔗 MC Discord Link</h1>

<h3 align="center">
Link Minecraft accounts with Discord<br>
and sync ranks automatically
</h3>

<p align="center">
<b>Free • Open-Source • Server-Agnostic</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Minecraft-Spigot%20%7C%20Paper-green">
  <img src="https://img.shields.io/badge/Discord.py-2.x-5865F2?logo=discord&logoColor=white">
  <img src="https://img.shields.io/badge/Database-SQLite%20%7C%20MySQL-blue">
  <img src="https://img.shields.io/badge/License-MIT-black">
</p>

---

## 🌍 What Is This?

**MC Discord Link** is a lightweight system that connects a player’s **Minecraft account** with their **Discord account** and automatically assigns Discord roles based on their **in-game rank**.

No panels.  
No bloated frameworks.  
Just clean linking + rank sync.

Designed for **any Minecraft server**.

---

## ⚔️ What It Does

✔ Link Minecraft ↔ Discord accounts  
✔ Generate secure one-time link codes  
✔ Sync LuckPerms ranks to Discord roles  
✔ Auto-assign roles on `/link`  
✔ Supports SQLite (local)  
✔ Supports MySQL / MariaDB (production)  

---

## ⚙️ How It Works (Simple)

1. Player runs a command in Minecraft  
2. Server generates a **6-digit code**  
3. Player runs `/link <code>` in Discord  
4. Bot verifies the code via database  
5. Discord role is assigned automatically  

That’s it.  
No staff intervention needed.

---

## 🧩 System Overview

Minecraft Plugin ───┐
├── Database (SQLite / MySQL)
Discord Bot ───┘


Both the **plugin** and the **bot** read from the same database.

---

## 🗃️ Database Setup

### 🟢 SQLite (Default – Local Testing)

SQLite works **only if the bot and server are on the same machine**.

```python ```
DB_PATH = "/path/to/link.db"
✅ Easy
❌ Not suitable for shared hosting

🔵 MySQL / MariaDB (Recommended)
If your Minecraft server and bot are hosted separately, you must use MySQL or MariaDB.

DB_CONFIG = {
    "host": "DB_HOST",
    "user": "DB_USER",
    "password": "DB_PASSWORD",
    "database": "DB_NAME",
    "port": 3306
}
Both services must use the same database credentials.

🤖 Discord Bot Setup
Create a bot in Discord Developer Portal

Enable:

Server Members Intent

Message Content Intent

Invite the bot with:

Manage Roles

Install dependencies:

pip install -r requirements.txt
Run the bot:

python bot.py
⚠️ IMPORTANT
The bot’s role must be higher than the roles it assigns.

⛏️ Minecraft Plugin Setup
Build or download the plugin JAR

Place it inside:

/plugins
Configure database settings

Restart the server

🚨 Common Problems & Fixes
❌ 403 Forbidden: Missing Permissions
Bot role is below the target role

Bot lacks Manage Roles

❌ Role not assigned
Rank name doesn’t match role name

Database mismatch between bot & server

❌ SQLite not syncing
Bot and server are on different machines
→ Use MySQL instead

🧠 Customization
You can easily:

Map Minecraft ranks → Discord roles

Change commands

Add logging

Extend verification logic

The code is intentionally simple and readable.

📜 License
MIT License

Free to use.
Free to modify.
Free to redistribute.

<p align="center"> <b>Built for the community.</b><br> If one server didn’t want it, others will. </p> ```
