import datetime

import cogs.checks as checks
from discord.ext import commands
import asyncio
import discord


class Git:
    """Various GitPython Commands.
    Git Commands for pulling the latest changes in the bot repo and pushing to a repo (these will need to be setup to your own fork if you plan to use this and customise it)
Proper Syntax for commands are:
    Push: git push remote branch
    Pull: git pull
"""
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    # @checks.has_permissions(administrator=True)
    async def git(self, ctx):
        """Main Git Command, holds all Git Functions"""
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid syntax')

    @git.command()
    async def push(self, ctx, remote: str, branch: str):
        """Pushes changes to the repo"""
        await ctx.send('Pushing to {} {}'.format(remote, branch))

    @push.error
    async def push_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'remote' and 'branch':
                await ctx.send("You are missing the remote and branch!")

    @git.command()
    async def pull(self, ctx):
        """Pulls the latest commit from the repo"""
        await ctx.send('Pulling Updates from Repo...')

    @git.command()
    async def repo(self, ctx):
        """Brings up the Repo of the bot (useful if people want to know where the fork is from)"""
        await ctx.send('''This bot was coded by Cabooshy#6969 in the discord.py rewrite! 
Nep's github repo is: https://github.com/Caboosh/CPU-Purple-Heart/''')

    @git.command()
    async def help(self, ctx):
        """Quick Help Command"""

        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days

        embed = discord.Embed(title="Here are the Available Commands:", colour=discord.Colour(0xb675c7))
        embed.set_author(name="CPU Purple Heart", icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.set_thumbnail(url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        embed.add_field(name="git push", value="git push <remote> <branch>")
        embed.add_field(name="git pull", value="Pulls from the Origin")
        embed.add_field(name="git repo", value="Displays the Repo of the bot")
        embed.add_field(name="git help", value="This Command")
        embed.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this")

# @commands.command(ctx)


def setup(bot):
    bot.add_cog(Git(bot))
