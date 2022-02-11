# Looping-Status-Task-Discord.py
Create a looping status task for your discord.py or disnake or pycord bot. All types of status types included.

# Step 1 - Getting Started 
First of all setup the bot. Additionally you can check the example.py
# Step 2 - Setting Up The Task
First of all in bot event: `on_ready` include a new line ```status_task.start()```,
[if you noy added then add:
```
@bot.event()
async def on_ready():
    status_task.start() #to start the looping task
```
then we need to setup the task. now after that add:
```
@tasks.loop()
async def status_task() -> None:
    await bot.change_presence(status=disnake.Status.dnd, activity=disnake.Game(" with electricity ⚡"))
    await asyncio.sleep(60)
    await bot.change_presence(activity=disnake.Streaming(name="Official Server With Dedication 🥰", url="https://zealtyro.com"))
    await asyncio.sleep(60)
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.listening, name="commands | Type !help for help 💁"))
    await asyncio.sleep(60)
    memberCount = str(len(list(bot.get_all_members())))
    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.watching, name=memberCount+" members enjoying my shocks 😳"))
```
