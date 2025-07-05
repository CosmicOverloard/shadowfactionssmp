import os
import discord
from discord.ext import commands
from mcstatus import JavaServer

MINECRAFT_SERVER = os.getenv("MINECRAFT_SERVER")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="mcstatus")
async def mcstatus(ctx):
    server = JavaServer(MINECRAFT_SERVER)
    try:
        status = server.status()
        await ctx.send(f"Server is online with {status.players.online} players!")
    except Exception:
        await ctx.send("Could not reach the Minecraft server.")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}!")

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Goodbye, {member.name}. We'll miss you!")

bot.run(DISCORD_TOKEN)
