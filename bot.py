
import discord
from discord import app_commands
import sqlite3
import time

TOKEN = "your_bot_token_here"  # Replace with your bot's token
GUILD_ID = "discord.gg/skyblock"  # Replace with your server's invite code or ID
DB_PATH = "path/to/your/database.db"

RANK_ROLE_MAP = {
    "owner": 1460285029493243915,
    "MAIN_ADMIN": 1460285562773704847,
    "DEVELOPER": 1460285656466198693,
    "ADMIN": 1460285731862876295,
    "SUPPORT_MANAGER": 1460285817149984824,
    "GAME_MASTER": 1460285928747831490,
    "HELPER": 1460286240099143741,
    "JUNIOR_HELPER": 1460286322974523515,
    "BETA_TESTER": 1460286396815249544,
    "YOUTUBER": 1460286240099143741,
    "SPECIAL": 1460286611534250108,
    "SPONSER_PLUS_PLUS_PLUS": 1460286704765374609,
    "SPONSER_PLUS_PLUS": 1460286822667255942,
    "SPONSER_PLUS": 1460286898139566090,
    "SPONSER": 1460286986958016575,
    "MVP_PLUS_PLUS": 1460283307404034132,
    "MVP_PLUS": 1460283058698584269,
    "MVP": 1460172248622039222,
    "VIP_PLUS": 1460282852242362511,
    "VIP": 1458390473847869511,
    "DEFAULT": 1460287077416571105
}

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def get_db():
    return sqlite3.connect(DB_PATH)


@tree.command(
    name="link",
    description="Link your Minecraft account",
    guild=discord.Object(id=GUILD_ID)
)
@app_commands.describe(code="6-digit code from Minecraft")
async def link(interaction: discord.Interaction, code: str):
    await interaction.response.defer(ephemeral=True)

    db = get_db()
    cur = db.cursor()
    now = int(time.time())

    # Validate code
    cur.execute(
        "SELECT mc_username, expires_at, used FROM link_codes WHERE code = ?",
        (code,)
    )
    row = cur.fetchone()

    if not row:
        await interaction.followup.send(" Invalid code.")
        return

    mc_username, expires_at, used = row

    if used:
        await interaction.followup.send("Code already used.")
        return

    if now > expires_at:
        await interaction.followup.send(" Code expired.")
        return

 
    cur.execute(
        "SELECT 1 FROM linked_accounts WHERE discord_id = ?",
        (str(interaction.user.id),)
    )
    if cur.fetchone():
        await interaction.followup.send(" Your Discord is already linked.")
        return



    cur.execute(
        "INSERT INTO linked_accounts VALUES (?, ?, ?)",
        (str(interaction.user.id), mc_username, now)
    )

    cur.execute(
        "UPDATE link_codes SET used = 1 WHERE code = ?",
        (code,)
    )


    cur.execute(
        "SELECT rank FROM rank_cache WHERE mc_username = ?",
        (mc_username,)
    )
    rank_row = cur.fetchone()

    db.commit()

    if not rank_row:
        await interaction.followup.send("⚠ Linked, but no rank found.")
        return

    rank = rank_row[0].lower()
    role_id = RANK_ROLE_MAP.get(rank)

    if not role_id:
        await interaction.followup.send(f"⚠ Linked, but no Discord role for rank `{rank}`.")
        return

    role = interaction.guild.get_role(role_id)
    member = interaction.guild.get_member(interaction.user.id)

    if role and member:
        await member.add_roles(role, reason="Minecraft rank sync")
        await interaction.followup.send(
            f"✅ Linked with **{mc_username}**\n🎖 Rank synced: **{rank}**"
        )
    else:
        await interaction.followup.send("⚠ Linked, but role assignment failed.")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Bot online as {client.user}")


client.run(TOKEN)

