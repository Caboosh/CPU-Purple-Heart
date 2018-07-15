import datetime
import sys
import traceback
import discord
import asyncio
from discord.ext import commands
from botconfig import token
from botconfig import prefix
from botconfig import botdesc
from botconfig import botversion
from botconfig import since

bot = commands.Bot(command_prefix=prefix, description=botdesc, dm_help=False)
bot.remove_command("help")

initial_extensions = [
    'cogs.admin',
    'cogs.cogloading',
    'cogs.help',
    'cogs.general'

]


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if error.param.name == 'arg':
            await ctx.send("You forgot to give me input to repeat, silly!")

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
    await bot.change_presence(game=discord.Game(name='The Sunset in Lastation... With Noire, of course.', type=3))


@bot.command()
async def ping(ctx):
    """Pings the bot and responds with the response time in ms"""
    await ctx.send('Pong! Took: {0} ms'.format(round(bot.latency, 3)))


@bot.command()
async def info(ctx):
    """Displays information about the bot in its current state"""
    author_repo = "https://github.com/Caboosh"
    nep_repo = author_repo + "/CPU-Purple-Heart"
    dpy_repo = "https://github.com/Rapptz/discord.py"
    python_url = "https://www.python.org/"
    days_since = (datetime.datetime.utcnow() - since).days
    dpy_version = "[{}]({})".format(discord.__version__, dpy_repo)
    python_version = "[{}.{}.{}]({})".format(*sys.version_info[:3], python_url)
    nep_version = "`[ Ver. {} ]`".format(botversion)
    app_info = await bot.application_info()
    owner = app_info.owner
    about = (
        "This is an instance of [Cpu Purple Heart, an open source Discord bot]({}) "
        "created by [Cabooshy]({}).".format(nep_repo, author_repo, ))

    embed = discord.Embed(colour=discord.Colour(0xb675c7))
    embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    embed.set_thumbnail(url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    embed.add_field(name="Instance owned by", value=str('`{}`'.format(owner)))
    embed.add_field(name="Python", value=python_version)
    embed.add_field(name="discord.py", value=dpy_version)
    embed.add_field(name="Neptune's version", value=nep_version)
    embed.add_field(name="About Neptune", value=about, inline=False)
    embed.set_footer(
        text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
        icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("I need the `Embed links` permission to send this")


@bot.group(invoke_without_command=True)
async def vitainfo(ctx):
    """Displays some handy info about the Vita homebrew and hacks available."""
    days_since = (datetime.datetime.utcnow() - since).days

    embed = discord.Embed(
        colour=discord.Colour(0xb675c7),
        description="""
**Henkaku and H-Encore**

    - Henkaku (For 3.60) - [Go Here on the vita](http://henkaku.xyz)
    
    - H-Encore (For 3.65 -3.68) [Download and Setup](https://github.com/TheOfficialFloW/h-encore).
Note that for H-Encore there are auto installers (makes the exploit app for you) on the [VitaHacks](https://reddit.com/r/VitaHacks) Subreddit. 
Such as [this one](https://github.com/noahc3/auto-h-encore/releases). which downloads and installs all you need for H-Encore to work!

**Essential Vita Homebrews!**

    - IMCUnlock - [Download](https://github.com/SKGleba/IMCUnlock). 
    Instructions are on the repo. (THIS IS A PCH-1XXX(PHAT) MOD, DO NOT ATTEMPT THIS ON THE PCH-2XXX(SLIM) MODELS).
    
    - IMCExtend - [Download](https://github.com/SKGleba/IMCExtend).
    Instructions are on the repo. (THIS IS A PCH-2XXX(SLIM) and PS(Vita)TV MOD, DO NOT ATTEMPT THIS ON THE PCH-1XXX MODELS).
    
    - NoNpDRM - [Download](https://github.com/TheOfficialFloW/NoNpDrm). 
    Install instructions are on the repo.
    
    - Adrenaline 6.61 - [v6.6 Download](https://github.com/TheOfficialFloW/Adrenaline/releases/tag/v6.6).  
    Instructions on the repo.
    
    - VitaShell - [Download](https://github.com/TheOfficialFloW/VitaShell/releases/tag/1.94). 
    This can be used as an alternative to the Molecule Branded version of this app. H-Encore gives you the option to install this when you run it.
    
    - Download Enabler - [Download](https://github.com/TheOfficialFloW/DownloadEnabler/releases/tag/v5.0). 
    Allows you to download from the built in web browser, setup is on the repo's readme, so read it!
    
    - VHBB - [Download](http://vhbb.download). 
    A Native Vita Homebrew Browser, think of it like FBI's TitleDB on the 3DS.""")
    embed.add_field(name="PAGE 2", value="{}vitainfo pg2".format(prefix))
    embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    embed.set_footer(
        text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
        icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("I need the `Embed links` permission to send this")


@vitainfo.command()
async def pg2(ctx):
    """Page 2 of the vita info"""
    days_since = (datetime.datetime.utcnow() - since).days

    embed = discord.Embed(
        colour=discord.Colour(0xb675c7),
        description="""
    **Essential Vita Homebrews! Pg-2**

        - ShellSecBat - [Download]). 
        Instructions are on the repo.

        - AdrBubbleBooter - [Download]().
        Instructions are on the repo.

        - RetroArch - [Download](). 
        Install instructions are on the repo.

        - CTManager - [Download]().  
        Instructions on the repo.

        - Theme Manager Ex (if CTManager wont install) - [Download](). 
        Instructions on the repo.

        - VitaQuakeII - [Download](). 
        Instructions on the repo.

        - VitaQuakeIII - [Download](). 
        Instructions on the repo.
        
        - VitaQuake - [Download](). 
        Instructions on the repo.""")
    embed.add_field(name="PAGE 1", value="{}vitainfo".format(prefix))
    embed.add_field(name="PAGE 3", value="{}vitainfo pg3".format(prefix))
    embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    embed.set_footer(
        text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
        icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("I need the `Embed links` permission to send this")


@bot.command()
async def game(ctx, status: str, type: int):
    """Sets Nep's playing status"""
    await bot.change_presence(game=discord.Game(name=status, type=type))
    await ctx.send("Status set.")


bot.run(token)
