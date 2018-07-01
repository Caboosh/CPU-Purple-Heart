import datetime
import traceback
import aiohttp
import cogs.checks as checks
import discord
from botconfig import prefix
from discord.ext.commands import errors
from discord.ext import commands


class Help:
    """A Simple cog for help commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def help(self, ctx):
        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="""A Discord based around the lovable Neptune and her 4th wall breaking abilities.
She also does normal bot stuff, because y'know, that's important too right.""", colour=discord.Colour(0xb675c7))
        embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.set_thumbnail(url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.add_field(name="Admin Commands:", value="---")
        embed.add_field(name="{}ban".format(prefix), value="Bans a member from the server.")
        embed.add_field(name="{}botavatar".format(prefix), value="Changes Nep's Avatar")
        embed.add_field(name="{}massban".format(prefix), value="Displays the Repo of the bot")
        embed.add_field(name="{}softban".format(prefix), value="""Soft Bans a member from the server, this is essentially
a kick with all messages deleted""")
        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))