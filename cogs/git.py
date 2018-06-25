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
    @checks.has_permissions(manage_server=True)
    async def git(self, ctx):
        """Main Git Command, holds all Git Functions"""
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid syntax')

    @git.command()
    async def push(self, ctx, remote: str, branch: str):
        """Pushes changes to the repo"""
        await ctx.send('Pushing to {} {}'.format(remote, branch))

    @git.command()
    async def pull(self, ctx):
        """Pulls the latest commit from the repo"""
        await ctx.send('Pulling Updates from Repo...')

    @git.command()
    async def help(self, ctx):
        """Quick Help Command"""
        await ctx.send('''```Commands:
    git push <remote> <branch>
    git pull```''')

# @commands.command(ctx)


def setup(bot):
    bot.add_cog(Git(bot))
