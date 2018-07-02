import datetime
import discord
from discord.ext import commands
from botconfig import prefix


class General:
    """General Commands, anyone can use these."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, *, user: discord.User=None):
        """Shows a User's Profile in a nice Embed"""
        author = ctx.author
        guild = ctx.guild

        if not user:
            user = author

        since = datetime.datetime(2018, 5, 15, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days
        joined_at = user.joined_at
        since_created = (ctx.message.created_at - user.created_at).days
        since_joined = (ctx.message.created_at - joined_at).days
        user_joined = joined_at.strftime("%d %b %Y %H:%M")
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        voice_state = user.voice

        created_on = "{}\n({} days ago)".format(user_created, since_created)
        joined_on = "{}\n({} days ago)".format(user_joined, since_joined)

        data = discord.Embed(description="All your User Info in a handy Embed!", colour=discord.Colour(0xb675c7))

        data.add_field(name="User ID", value=user.id, inline=False)
        data.add_field(name="Joined Discord on", value=created_on, inline=True)
        data.add_field(name="Joined this server on", value=joined_on, inline=True)
        if voice_state and voice_state.channel:
            data.add_field(
                name="Current voice channel",
                value="{0.name} (ID {0.id})".format(voice_state.channel),
                inline=False,
            )
        else:
            data.add_field(
                name="Current Voice Channel",
                value="None."
            )

        data.set_footer(
            text="Breaking the 4th wall on discord since 15 May 2018 ({} days ago!)".format(days_since),
            icon_url="https://caboosh.s-ul.eu/oSqCT9e5.png")

        name = str(user)
        name = " ~ ".join((name, user.nick)) if user.nick else name

        if user.avatar:
            avatar = user.avatar_url
            avatar = avatar.replace("webp", "png")
            data.set_author(name=name, icon_url=avatar)
            data.set_thumbnail(url=avatar)
        else:
            data.set_author(name=name)

        try:
            await ctx.send(embed=data)
        except discord.HTTPException:
            await ctx.send("I need the `Embed links` permission to send this.")

    @commands.group(invoke_without_command=True)
    async def echo(self, ctx):
        """Echos an input from the user."""
        await ctx.send("""```python
Usage: {}echo 'Subcommand' 'Word/String/Int to Echo'```""".format(prefix))

    @echo.command()
    async def word(self, ctx, arg):
        try:
            await ctx.send(arg)
        except discord.HTTPException:
            user = discord.Client.get_user(discord.User.discriminator)
            if user is not None:
                await user.send("I need to be able to send messages to echo!")

    @echo.command()
    async def string(self, ctx, arg):
        await ctx.send(arg)


def setup(bot):
    bot.add_cog(General(bot))
