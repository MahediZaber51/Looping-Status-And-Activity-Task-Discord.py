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
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(" with electricity ⚡"))
    await asyncio.sleep(60)
    await bot.change_presence(activity=discord.Streaming(name="Official Server With Dedication 🥰", url="https://zealtyro.com"))
    await asyncio.sleep(60)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="commands | Type !help for help 💁"))
    await asyncio.sleep(60)
    memberCount = str(len(list(bot.get_all_members())))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=memberCount+" members enjoying my shocks 😳"))
```
Now let's understand what we coded there:
`await bot.change_presence(status=STATUS-HERE, activity=ACTIVITY-HERE)` this is the main format.
we just need to change the `STATUS-HERE` and `ACTIVITY-HERE` text to set a status with custom activity.
Here's the list of all available Statuses:
```
discord.Status.dnd #to set status to DND
discord.Status.idle #to set status to Idle
discord.Status.online #to set status to Online
```
Here's the list of all available Activity Types:
```

```
