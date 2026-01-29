Discord PowerShell Bot

A simple Discord bot that executes PowerShell commands sent through a Discord channel and returns the output.

What it does

Connects to Discord using a bot token

Creates a text channel on startup

Executes PowerShell commands sent in that channel

Sends command output back to Discord

Requirements

Windows

Python 3

Python packages:

discord.py

requests

pyinstaller

Uses built-in Python module:

subprocess

Install dependencies:

pip install discord.py requests pyinstaller

Setup

Create a Discord bot and copy the token

Replace the token in the script:

DISCORD_TOKEN = "YOUR_BOT_TOKEN"


Run the script:

python bot.py

Optional: Build EXE
pyinstaller --onefile --noconsole bot.py

Usage

Type any PowerShell command in the created Discord channel

The bot replies with the output

Notes

PowerShell session is persistent

PowerShell window is hidden

Commands only work in the created channel

Warning

This bot can execute any PowerShell command.
Use only on systems you own or have permission to use.
