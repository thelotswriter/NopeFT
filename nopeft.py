from discord.ext import commands
import os

token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix=['<@!971516187248832532> ', '<@971516187248832532> '])


@client.event
async def on_ready():
    print(f"{client.user} is connected!")


@client.event
async def on_message(message):
    txt = message.content.lower()
    channel = message.channel
    author = message.author
    if str(author) != 'NopeFT#7516':
        if 'nft' in txt:
            await channel.send('Boo NFT bad!')
    await client.process_commands(message)


@client.command()
async def test(context, *, message):
    print(message)

client.run(token)