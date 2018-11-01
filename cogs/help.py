import datetime
import discord
from botconfig import prefix
from discord.ext import commands


class Help:
    """A Simple cog for help commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="""A Discord bot based around the lovable Neptune and her 4th wall breaking abilities.
She also does normal bot stuff, because y'know, that's important too right.""", colour=discord.Colour(0xb675c7))
        embed.set_author(name="CPU Purple Heart", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="Admin Commands:", value="{}help admin".format(prefix), inline=False)
        embed.add_field(name="General Commands:", value="{}help general".format(prefix), inline=False)
        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")

    @help.command()
    async def general(self, ctx):
        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(
            title="""A Discord bot based around the lovable Neptune and her 4th wall breaking abilities.
        She also does normal bot stuff, because y'know, that's important too right.""", 
            colour=discord.Colour(0xb675c7)
        )
        embed.set_author(
            name="CPU Purple Heart",
            icon_url=self.bot.user.avatar_url
        )
        embed.add_field(
            name="General Commands:", 
            value="---", 
            inline=False
        )
        embed.add_field(
            name="{}profile".format(prefix), 
            value="Shows the user's profile in a nice embed", 
            inline=False
        )
        embed.add_field(
            name="{}info".format(prefix), 
            value="Shows information about the bot and the environment it is running in, useful for testing forks and such.", 
            inline=False
        )
        embed.add_field(
            name="{}ping".format(prefix), 
            value="Pings the bot and returns the response time in \"0.<response time> s\" format.", 
            inline=False
        )
        embed.add_field(
            name="{}vitainfo [pg<number>]".format(prefix), 
            value="""Shows some basic essentials for Vita Homebrew, mainly for the \"PeachProduction\" and \"Cabooshy's Den\" Discord Servers.""", 
            inline=False
        )
        embed.add_field(
            name="{}echo <word/string>".format(prefix),
            value="""Echos input passed to the bot, can be used to make the bot say things.""", 
            inline=False
        )
        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url
        )
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")

    @help.command()
    async def admin(self, ctx):
        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="""A Discord bot based around the lovable Neptune and her 4th wall breaking abilities.
           She also does normal bot stuff, because y'know, that's important too right.""",
                              colour=discord.Colour(0xb675c7))
        embed.set_author(name="CPU Purple Heart", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="Admin Commands:", value="---", inline=False)
        embed.add_field(name="{}ban".format(prefix), value="Bans a member from the server.", inline=False)
        embed.add_field(name="{}massban".format(prefix),
                        value="""Mass bans multiple members from the server.""", inline=False)
        embed.add_field(
            name="{}softban".format(prefix),
            value="""Soft bans a member from the server.""", inline=False)

        embed.add_field(
            name="{}botavatar".format(prefix),
            value="""Sets Nep's avatar.""", inline=False)

        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url=self.bot.user.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")


def setup(bot):
    bot.add_cog(Help(bot))
