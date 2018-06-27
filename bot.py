import datetime
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
botversion = '0.1a'
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


@bot.command()
async def info(self, ctx):
    """Displays information about the bot in its current state"""
    author_repo = "https://github.com/Caboosh"
    nep_repo = author_repo + "/CPU-Purple-Heart"
    dpy_repo = "https://github.com/Rapptz/discord.py"
    python_url = "https://www.python.org/"
    since = datetime.datetime(2018, 5, 15, 0, 0)
    days_since = (datetime.datetime.utcnow() - since).days
    dpy_version = "[{}]({})".format(discord.__version__, dpy_repo)
    python_version = "[{}.{}.{}]({})".format(*sys.version_info[:3], python_url)
    red_version = "[{}]({})".format(discord.__version__)
    app_info = await self.bot.application_info()
    owner = app_info.owner
    about = (
        "This is an instance of [Cpu Purple Heart, an open source Discord bot]({}) "
        "created by [Cabooshy]({})."
        "".format(nep_repo, author_repo,)
    )


    embed = discord.Embed(colour=discord.Colour(0xb675c7)
    embed.add_field(name="Instance owned by", value=str(owner))
    embed.add_field(name="Python", value=python_version)
    embed.add_field(name="discord.py", value=dpy_version)
    embed.add_field(name="Red version", value=red_version)
    embed.add_field(name="About Red", value=about, inline=False)
    embed.set_footer(
        text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since)
    )
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("I need the `Embed links` permission to send this")



    embed.set_author(name="CPU Purple Heart", url="https://discordapp.com",
                     icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    embed.set_footer(text="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    embed.add_field(name="Owner", value="`Cabooshy#6969`", inline=True)
    embed.add_field(name="Library",
                    value="[Discord.py Rewrite (1.0.0a)](https://discordpy.readthedocs.io/en/rewrite)",
                    inline=True)
    embed.add_field(name="Language Version",
                    value="[Python 3.6.3](https://www.python.org/downloads/release/python-363/)", inline=True)
    embed.add_field(name="Bot version",
                    value='[](https://github.com/Caboosh/CPU-Purple-Heart/releases/tag/0.1a)', inline=True)
    await ctx.send(embed=embed)

bot.run(token)
