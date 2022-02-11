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
then we need to setup the task. now after that add this structure:
```
@tasks.loop()
async def status_task() -> None:
    #put the upcoming codes here
```
Now let's complete the code:
```
await bot.change_presence(status=STATUS-HERE, activity=ACTIVITY-HERE)
await asyncio.sleep(TIME)
```
This is the main format and by adding this multiple times you will be able to create a looping task. We just need to change the `STATUS-HERE` and `ACTIVITY-HERE` text to set a status with custom activity.
Here's the list of all available Statuses:
```
discord.Status.dnd #to set status to DND
discord.Status.idle #to set status to Idle
discord.Status.online #to set status to Online
```
Here's the list of all available Activity Types:
```
#streaming activity. put name of the stream and the twitch url
discord.Streaming(name="stream name", url="stream url")

# Gaming activity. put the name of the game
discord.Game("Name of the Game")

#listening activity. put the name of the song
disnake.Activity(type=discord.ActivityType.listening, name="name of the music")
```
