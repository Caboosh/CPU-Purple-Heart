import asyncio
import datetime
import sys
import traceback
import discord
import twitch
from discord.ext import commands
from botconfig import token
from botconfig import prefix
from botconfig import botdesc
from botconfig import botversion
from botconfig import since
from botconfig import owner

bot = commands.Bot(command_prefix=prefix, description=botdesc, dm_help=False, owner_id=owner)
bot.remove_command("help")

initial_extensions = [
    'cogs.admin',
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



# Set On Ready Status, Print Details into Console and Set Presence to allow Visual that Bot is Running.
@bot.event
async def on_ready():
    print('=======================')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('=======================')
    print('Bot Owner: {}' .format(bot.owner_id))
    await bot.change_presence(game=discord.Game(name='The Sunset in Lastation... With Noire, of course.', type=3))


@bot.command()
async def ping(ctx):
    """Pings the bot and responds with the response time in ms"""
    await ctx.send('Pong! Took: {0} s'.format(round(bot.latency, 3)))


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
    embed.set_author(name="CPU Purple Heart", icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="Instance owned by", value=str('`{}`'.format(owner)))
    embed.add_field(name="Python", value=python_version)
    embed.add_field(name="discord.py", value=dpy_version)
    embed.add_field(name="Neptune's version", value=nep_version)
    embed.add_field(name="About Neptune", value=about, inline=False)
    embed.set_footer(
        text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
        icon_url=bot.user.avatar_url)
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("I need the `Embed links` permission to send this")


@bot.command()
async def game(ctx, status: str, url: str, type: int):
    """Sets Nep's playing status"""
    await bot.change_presence(game=discord.Game(name=status, url=url, type=type))
    await ctx.send("Status set.")


bot.run(token, bot=True, reconnect=True)
