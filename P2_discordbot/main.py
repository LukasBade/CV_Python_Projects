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

bot = commands.Bot(command_prefix="-", intents=intents)

role_name = "Mitglied"
admin_role = "Admin"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!") #.send for private message


@bot.event
async def on_message(message):
    if message.author == bot.user: #bot to not reply to itself
        return
    if "shit" in message.content.lower():
        await message.delete()
        warning_msg = await message.channel.send(f"{message.author.mention}, watch your language!")

    await bot.process_commands(message) #to allow commands to work

# "-hello" to mention bot
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")


@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been assigned the '{role.name}' role!")
    else:
        await ctx.send(f"Role '{role_name}' not found.")


@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, the '{role.name}' role has been removed from you!")
    else:
        await ctx.send(f"Role '{role_name}' not found.")


@bot.command()
@commands.has_role(admin_role)
async def secret(ctx):
    await ctx.send("This is a secret message for admins only!")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the required role to run this command.")


@bot.command()
async def direct(ctx, *, message):
    await ctx.author.send("You said: " + message)


@bot.command()
async def reply(ctx):
    await ctx.reply("Thanks for your message!", mention_author=True)


@bot.command()
async def polling(ctx, *, question):
    embed = discord.Embed(title="Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)