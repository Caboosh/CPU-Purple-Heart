import aiohttp
import discord
from discord.ext import commands


class Admin:
    """The Admin Commands, Right now only callable by Cabooshy, for reasons.. i guess."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """Bans a member from the server.
        You can also ban from ID to ban regardless whether they're
        in the server or not.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Ban Members permission.
        """
        if reason is None:
            reason = f'Action done by {ctx.author} (ID: {ctx.author.id})'

        await ctx.guild.ban(discord.Object(id=member), reason=reason)
        await ctx.send('\N{OK HAND SIGN}, User has been banned for: {}'.format(reason))

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('You Didn\'t Specify a user to ban stupid.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You dont have the proper Permissions to use this command!')


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, reason: str, *members: discord.Member):
        """Mass bans multiple members from the server.
        You can also ban from ID to ban regardless whether they're
        in the server or not.
        Note that unlike the ban command, the reason comes first
        and is not optional.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Ban Members permission.
        """

        for member_id in members:
            await ctx.guild.ban(discord.Object(id=member_id), reason=reason)

        await ctx.send('\N{OK HAND SIGN}')

    @massban.error
    async def massban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('You Didn\'t Specify the users to ban.')

    @massban.error
    async def massban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You dont have the proper Permissions to use this command!')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason: str = None):
        """Soft bans a member from the server.
        A softban is basically banning the member from the server but
        then unbanning the member as well. This allows you to essentially
        kick the member while removing their messages.
        In order for this to work, the bot must have Ban Member permissions.
        To use this command you must have Kick Members permissions.
        """

        if reason is None:
            reason = f'Action done by {ctx.author} (ID: {ctx.author.id})'

        obj = discord.Object(id=member)
        await ctx.guild.ban(obj, reason=reason)
        await ctx.guild.unban(obj, reason=reason)
        await ctx.send('\N{OK HAND SIGN}')

    @softban.error
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('You Didn\'t Specify a user to ban silly.')

    @softban.error
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You dont have the proper Permissions to use this command!')

    @commands.command()
    @commands.is_owner()
    async def botavatar(self, ctx, url: str):
        """Sets Vert's avatar"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.read()
            try:
                await ctx.bot.user.edit(avatar=data)
            except discord.HTTPException:
                await ctx.send(
                    "Failed. Remember that you can edit the avatar "
                    "up to two times a hour. The URL must be a "
                    "direct link to a JPG / PNG."
                )
            except discord.InvalidArgument:
                await ctx.send("JPG / PNG format only.")
            else:
                await ctx.send("Done.")


def setup(bot):
    bot.add_cog(Admin(bot))
