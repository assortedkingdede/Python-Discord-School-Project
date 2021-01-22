import discord
import asyncio
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def testmsg(ctx):
    await ctx.send('I am now going to BONZIFY your Computer')

@bot.command()
async def testimage(ctx):
    await ctx.send(file=discord.File('R2846d6178ef9e330f44e2e9c32ff8181.png'))
    await ctx.send('I am surfing the internet for more Computers to BONZIFY')

@bot.command()
async def testgif(ctx):
    await ctx.send(file=discord.File('squidward.gif'))

@bot.command()
async def testvideo(ctx):
    await ctx.send(file=discord.File('video0-8.mp4'))

bot.run('Insert Token Here')

