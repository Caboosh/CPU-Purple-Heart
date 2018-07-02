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
        embed.add_field(name="Admin Commands:", value=".", inline=False)
        embed.add_field(name="{}ban".format(prefix), value="Bans a member from the server.", inline=False)
        embed.add_field(name="{}botavatar".format(prefix), value="Changes Nep's Avatar", inline=False)
        embed.add_field(name="{}massban".format(prefix), value="Displays the Repo of the bot", inline=False)
        embed.add_field(name="{}softban".format(prefix), value="""Soft Bans a member from the server""", inline=False)
        embed.add_field(name="(Owner Only) Git Commands:", value=".", inline=False)
        embed.add_field(
            name="{}git push <remote> <branch>".format(prefix),
            value="Pushes Changes to a repo .",
            inline=False
        )
        embed.add_field(
            name="{}git pull".format(prefix),
            value="Pulls changes (if any) from a repo.",
            inline=False
        )
        embed.add_field(
            name="{}git repo".format(prefix),
            value="provides a handy link to the main/forked repo.",
            inline=False
        )
        embed.add_field(
            name="{}git help".format(prefix),
            value="Shows the local Git Help Commands.",
            inline=False
        )
        embed.add_field(name="Page 2", value="Type {}help <number in word form> to see the next page".format(prefix), inline=False)
        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")

    @help.command
    async def two(self, ctx):
        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="""A Discord based around the lovable Neptune and her 4th wall breaking abilities.
She also does normal bot stuff, because y'know, that's important too right.""", colour=discord.Colour(0xb675c7))
        embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.add_field(name="Admin Commands:", value=".", inline=False)
        embed.add_field(name="{}ban".format(prefix), value="Bans a member from the server.", inline=False)
        embed.add_field(name="{}botavatar".format(prefix), value="Changes Nep's Avatar", inline=False)
        embed.add_field(name="{}massban".format(prefix), value="Displays the Repo of the bot", inline=False)
        embed.add_field(name="{}softban".format(prefix), value="""Soft Bans a member from the server""",inline=False)
        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")


def setup(bot):
    bot.add_cog(Help(bot))
