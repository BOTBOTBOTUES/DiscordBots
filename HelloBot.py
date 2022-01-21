import discord

TOKEN = "OTIwODA1OTk0NjQ3NDA4Njkx.YbptaA.VvgT3JLKs722eqsh0Fw1GxfGraQ"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')

client.run(TOKEN)
