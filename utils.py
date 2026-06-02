# utils.py
import os
import questionary
from colorama import init, Fore, Style as AnsiStyle
from questionary import Style

init(autoreset=True)  # resets color after each print automatically

menu_style = Style([
    ("qmark",        "fg:#00ffff bold"),   # the ? mark
    ("question",     "fg:#ffff00 bold"),   # question text
    ("highlighted",  "fg:#ff00ff bold"),   # currently selected item
    ("selected",     "fg:#ff00ff"),        # after selection is confirmed
    ("pointer",      "fg:#ff00ff bold"),   # the >> arrow
    ("answer",       "fg:#00ffff bold"),   # confirmed answer
])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def parse_tags(text):
    return [
        tag.strip()
        for tag in text.split(",")
        if tag.strip()
    ]

def _score_color(value, max_value=10):
    """Return color based on score: red → yellow → green."""
    ratio = value / max_value
    if ratio >= 0.7:
        return Fore.GREEN
    elif ratio >= 0.4:
        return Fore.YELLOW
    else:
        return Fore.RED

def _colored_score(label, value, max_value=10):
    color = _score_color(value, max_value)
    return f"{Fore.WHITE}{label}: {color}{value}{AnsiStyle.RESET_ALL}"

def _revisitability_label(value):
    labels = {
        0: (Fore.RED,    "Never"),
        1: (Fore.YELLOW, "Rarely"),
        2: (Fore.CYAN,   "Sometimes"),
        3: (Fore.GREEN,  "Often"),
    }
    color, text = labels.get(value, (Fore.WHITE, str(value)))
    return f"{Fore.WHITE}Revisitability: {color}{text}{AnsiStyle.RESET_ALL}"

def print_game(game):
    print()
    print(Fore.CYAN + AnsiStyle.BRIGHT + "=" * 50)
    print(Fore.WHITE + AnsiStyle.BRIGHT + game["name"])
    print(Fore.CYAN + AnsiStyle.BRIGHT + "=" * 50)
    print(_colored_score("Love",      game["love"]))
    print(_colored_score("Graphics",  game["graphics"]))
    print(_colored_score("Gameplay",  game["gameplay"]))
    print(_revisitability_label(game["revisitability"]))

    last = game["last_played"]
    last_str = f"{Fore.YELLOW}{last}" if last else f"{Fore.RED}Never"
    print(f"{Fore.WHITE}Last played: {last_str}")

    if game["tags"]:
        tags_str = "  ".join(f"{Fore.MAGENTA}#{t}" for t in game["tags"])
        print(f"{Fore.WHITE}Tags: {tags_str}")

    if game["notes"]:
        print(f"\n{Fore.WHITE + AnsiStyle.DIM}Notes:")
        print(f"{AnsiStyle.DIM}{game['notes']}")

    print()

def select_game(games):
    if not games:
        print(Fore.RED + "\nNo games found.\n")
        return None

    _print_game_list(games)

    name = questionary.autocomplete(
        "Search:",
        choices=sorted([g["name"] for g in games])
    ).ask()
    if name is None:
        return None
    return next((g for g in games if g["name"] == name), None)

def select_game_from_list(games):
    if not games:
        print(Fore.RED + "\nNo games found.\n")
        return None
    name = questionary.select(
        "Select game:",
        choices=sorted([g["name"] for g in games])
    ).ask()
    if name is None:
        return None
    return next((g for g in games if g["name"] == name), None)


def _print_game_list(games):
    print()
    for g in sorted(games, key=lambda g: g["name"]):
        love_color = _score_color(g["love"])
        print(f"  {love_color}♥ {g['love']}  {Fore.WHITE}{g['name']}")
    print()

