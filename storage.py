# storage.py
# responsible for r\w of json

import json
from pathlib import Path

DB_FILE = Path("data.json")


def load_games():
    if not DB_FILE.exists():
        return []

    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_games(games):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(
            games,
            f,
            indent=2,
            ensure_ascii=False
        )