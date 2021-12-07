import json
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_PATH = Path(__file__).parent
SETTINGS_FILE_PATH = (BASE_PATH / "../settings.json").resolve()
AOC_SESSION = os.environ.get("AOC_SESSION")

with open(SETTINGS_FILE_PATH) as f:
    settings = json.load(f)


def download_input(day_num: int):
    base_url = settings["base_url"]
    year = settings["year"]
    res = requests.get(
        f"{base_url}{year}/day/{day_num}/input", cookies={"session": AOC_SESSION}
    )
    res.raise_for_status()
    with open("input.txt", "w") as f:
        f.write(res.content)


download_input(1)
