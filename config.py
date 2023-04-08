import pathlib
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = str(os.getenv("DISCORD_TOKEN"))
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
