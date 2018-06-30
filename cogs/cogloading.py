import datetime
import traceback
import aiohttp
import cogs.checks as checks
import discord
from discord.ext.commands import errors
from discord.ext import commands


class CogLoading:
    """Owner Only Cog Loading Commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(administrator=True)
    async def load(self, ctx, *, module):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command()
    @checks.has_permissions(administrator=True)
    async def unload(self, ctx, *, module):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(name='reload')
    @checks.has_permissions(administrator=True)
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')


def setup(bot):
    bot.add_cog(CogLoading(bot))
