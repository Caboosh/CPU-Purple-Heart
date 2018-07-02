.. _debian-based-install:

==================================================================================
Installing the bot on Debian Based Distros (Ubuntu, Linux Mint, ElementaryOS etc.)
==================================================================================

Installing Nep on Debian and Ubuntu based Linux Distro is similarly easy to the Windows install, and this page will help walk you through the steps of doing so.

First off, make sure you have your sources up to date, do this by running:

.. code-block:: bash
sudo apt-get update

Then, install python3.6 on Ubuntu 14.04 and 16.04 with:
.. code-block:: bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

For 16.10 and 17.04, we do:
.. code-block:: bash
sudo apt-get update
sudo apt-get install python3.6

as Python 3.6 is in the universe repo for these versions of ubuntu.

17.10 and up have 3.6 installed by default.
