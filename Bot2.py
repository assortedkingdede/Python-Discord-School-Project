import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run('ODAxNDk4NzA0MzgwMjk3MjI3.YAhj1g.zfK04FMzIS3Zjq4eS7jmNe8ODrs')
