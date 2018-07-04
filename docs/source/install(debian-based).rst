.. _debian-based-install:

==================================================================================
Installing the bot on Debian Based Distros (Ubuntu, Linux Mint, ElementaryOS etc.)
==================================================================================

Installing Nep on Debian and Ubuntu based Linux Distros is similarly easy to the Windows install, and this page will help walk you through the steps of doing so.

First off, make sure you have your sources up to date, do this by running:

.. code-block:: console

  $ sudo apt-get update

Then, install python3.6 on Ubuntu 14.04 and 16.04 with:

.. code-block:: console
  
  $ sudo add-apt-repository ppa:deadsnakes/ppa
  $ sudo apt-get update
  $ sudo apt-get install python3.6

For 16.10 and 17.04, we do:

.. code-block:: console
  
  $ sudo apt-get update
  $ sudo apt-get install python3.6

as Python 3.6 is in the universe repo for these versions of ubuntu.

17.10 and up have 3.6 installed by default.


Then, we need to download Nep, you can do this however you want, but i'd recommend downloading the latest release of the bot from the releases, and extracting the bot to a place you can easily access, such as your desktop.

This is usually located under:

.. code-block:: console

    /home/USERNAME/Desktop

Or if you are using the terminal on a server it will be ~/Desktop

We can then proceed to setting up the botconfig.py file, which you can copy and paste from the example bundled with the bot, which looks like this:

.. code-block:: python

    # This is named the way it is so it doesn't conflict with an existing installation, and serves as a way to showcase the layout of this botconfig.py file
    # Rename this file to botconfig.py to use it and remove these comments

    prefix = 'Enter your Prefix here'
    token = 'Put your token here'
    botdesc = '''The Description of the bot if being used for other uses apart from being Nep'''

You can remove the comments, and fill out the parts as required, the bot will have a default prefix of _ if no prefix is found here, so you are not stuck without access to the bot's commands.
