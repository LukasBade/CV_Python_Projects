from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

token = os.getenv("DISCORD_TOKEN")

if token is None:
    raise ValueError("DISCORD_TOKEN not loaded. Check .env path!")

handler = logging.FileHandler("discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)