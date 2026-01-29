# Discord PowerShell Bot

A simple Discord bot that executes **PowerShell commands** sent through a Discord channel and returns the output.

## What it does
- Connects to Discord using a bot token  
- Creates a text channel on startup  
- Executes PowerShell commands sent in that channel  
- Sends command output back to Discord  

## Design
- **Client:** Discord bot using `discord.py`  
- **Command Engine:** Persistent PowerShell process  
- **Execution:** Commands sent as Discord messages  
- **Process Handling:** Managed via Python `subprocess`  
- **Output Handling:** Captured from stdout and returned to Discord  
- **Scope Control:** Commands only accepted in the created channel  
- **UI:** No console window (hidden PowerShell)  

## Requirements
- Windows  
- Python 3  
- Python packages:
  - `discord.py`
  - `requests`
  - `pyinstaller`
- Built-in module:
  - `subprocess`

Install dependencies:
```bash
pip install discord.py requests pyinstaller
```

##Setup

- Create a Discord bot and copy the token
- Replace the token in the script:
```bash
DISCORD_TOKEN = "YOUR_BOT_TOKEN"
```

##Run the script:
```bash
python bot.py
```

##Optional: Build EXE
```bash
pip install discord.py requests pyinstaller
```
##Usage

- Type any PowerShell command in the created Discord channel
- The bot replies with the output

##Notes

- PowerShell session is persistent
- PowerShell window is hidden
- Commands only work in the created channel
