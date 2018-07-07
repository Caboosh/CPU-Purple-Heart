import sys
import discord
from colorama import init, Back

init()
# Let's do all the dumb version checking in one place.

if discord.version_info.major < 1:
    print(
        "You are not running the rewritten version of discord.py.\n\n"
        "In order to use the bot you MUST be running d.py version"
        " >= 1.0.0a. (d.py rewrite)"
    )
    sys.exit(1)

if sys.version_info < (3, 5, 0):
    print(Back.RED + "[DEPRECATION WARNING]")
    print(
        Back.RED + "You are currently running Python 3.4 or lower."
        " Support for Python 3.4 and lower will end with the main release."
        " Please update your environment to Python 3.6 as soon as possible to avoid"
        " any interruptions after the main release."
    )
