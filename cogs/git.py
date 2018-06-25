import cogs.checks as checks
from discord.ext import commands
import asyncio
import discord
import textwrap
import io


class Git:
    """Git Commands, Used for pulling updates and pushing changes to and from a repo"""
    def __init__(self, bot):
        self.bot = bot


@commands.group()
@checks.has_permissions(manage_server=True)
async def git(self, ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('''```Invalid git command passed...
Proper Syntax for commands are:
    Push: git push remote branch
    Pull: git pull```''')
"""Various GitPython Commands.
    Git Commands for pulling the latest changes in the bot repo and pushing to a repo (these will need to be setup to 
    your own fork if you plan to use this and customise it) 
"""


@git.command()
async def push(ctx, remote: str, branch: str):
    await ctx.send('Pushing to {} {}'.format(remote, branch))


@git.command
async def pull(ctx):
    await ctx.send('Pulling Updates from Repo...')
