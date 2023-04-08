import discord
from discord.ext import commands
import config
from host_utils import keep_alive, restart_bot


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    for cmd_file in config.CMDS_DIR.glob("*.py"):
        if cmd_file.name != "__init__.py":
            await client.load_extension(f"cmds.{cmd_file.name[:-3]}")


def main():
    keep_alive()
    try:
        client.run(config.TOKEN)
    except discord.errors.HTTPException:
        restart_bot()


if __name__ == "__main__":
    main()
