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

if sys.version_info < (3, 6, 0):
    print(Back.RED + "[DEPRECATION WARNING]")
    print(
        Back.RED + "You are currently running Python 3.5."
        " Support for Python 3.5 will end with the release of beta 16."
        " Please update your environment to Python 3.6 as soon as possible to avoid"
        " any interruptions after the beta 16 release."
    )
