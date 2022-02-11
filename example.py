import discord
import asyncio
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context

bot = Bot(command_prefix="prefix")

@bot.event
async def on_ready() -> None:
    status_task.start()

@tasks.loop()
async def status_task() -> None:
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(" with electricity ⚡"))
    await asyncio.sleep(60)
    await bot.change_presence(activity=discord.Streaming(name="Official Server With Dedication 🥰", url="https://zealtyro.com"))
    await asyncio.sleep(60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="commands | Type !help for help 💁"))
    await asyncio.sleep(60)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="all members enjoying my shocks 😳"))


bot.run("TOKEN")
