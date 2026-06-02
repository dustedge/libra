# actions.py
# game collection operations

import random
from datetime import datetime
import questionary
from storage import save_games
from utils import (
    parse_tags,
    print_game,
    select_game,
    select_game_from_list,
    menu_style
)

def _ask_int(prompt, default="5"):
    """Ask for an integer, return None if user cancels."""
    answer = questionary.text(prompt, default=default).ask()
    if answer is None:
        return None
    try:
        return int(answer)
    except ValueError:
        return int(default)

def add_game(games):
    name = questionary.text("Game name:").ask()
    if not name:
        return

    love = _ask_int("Love (0-10):", "5")
    if love is None:
        return

    graphics = _ask_int("Graphics (0-10):", "5")
    if graphics is None:
        return

    gameplay = _ask_int("Gameplay (0-10):", "5")
    if gameplay is None:
        return

    revisitability_answer = questionary.select(
        "Revisitability:",
        choices=["0", "1", "2", "3"]
    ).ask()
    if revisitability_answer is None:
        return

    tags_answer = questionary.text("Tags:").ask()
    if tags_answer is None:
        return

    notes_answer = questionary.text("Notes:").ask()
    if notes_answer is None:
        return

    game = {
        "name": name,
        "love": love,
        "graphics": graphics,
        "gameplay": gameplay,
        "revisitability": int(revisitability_answer),
        "last_played": None,
        "tags": parse_tags(tags_answer or ""),
        "notes": notes_answer or ""
    }
    games.append(game)
    save_games(games)

def browse_games(games):
    game = select_game_from_list(games)
    if game:
        print_game(game)

def search_game(games):
    game = select_game(games)
    if game:
        print_game(game)

def recommend_game(games):
    if not games:
        print("\nNo games in library.\n")
        return

    candidates = [g for g in games if g["love"] >= 7]
    if not candidates:
        candidates = games
    print_game(random.choice(candidates))

def recommend_game_random(games):
    if not games:
        print("\nNo games in library.\n")
        return
    print_game(random.choice(games))

def mark_played(games):
    game = select_game(games)
    if not game:
        return
    game["last_played"] = datetime.now().strftime("%Y-%m-%d")
    save_games(games)

def forgotten_favorite(games):
    favorites = [g for g in games if g["love"] >= 8]
    if not favorites:
        return
    favorites.sort(key=lambda g: g["last_played"] or "1900-01-01")
    print_game(favorites[0])