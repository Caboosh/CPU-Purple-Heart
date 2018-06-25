import sys
import traceback
import discord
import asyncio
from discord.ext import commands
from botconfig import token
from botconfig import prefix
from botconfig import botdesc
import cogs.checks as checks


initial_extensions = [
    'cogs.admin',
    'cogs.git',

]

bot = commands.Bot(command_prefix=prefix, description=botdesc, pm_help=True)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print('=======================')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('=======================')


@bot.command()
async def ping(ctx):
    """Pings the bot and responds with the response time in ms"""
    await ctx.send('Pong! Took: {0}ms'.format(round(bot.latency, 3)))


bot.run(token)
