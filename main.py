# main.py
import questionary
from storage import load_games
from utils import clear_screen, menu_style
from actions import (
    add_game,
    browse_games,
    search_game,
    recommend_game,
    recommend_game_random,
    forgotten_favorite,
    mark_played
)

def main():
    while True:
        games = load_games()
        choice = questionary.select(
            "Game Library",
            choices=[
                "Add game",
                "Browse games",
                "Recommend game",
                "Search game",
                "Forgotten favorite",
                "Mark as played",
                "Random game",
                "Exit"
            ],
            style=menu_style
        ).ask()
        if choice is None or choice == "Exit":
            break
        elif choice == "Add game":
            clear_screen()
            add_game(games)
        elif choice == "Browse games":
            clear_screen()
            browse_games(games)
        elif choice == "Recommend game":
            clear_screen()
            recommend_game(games)
        elif choice == "Random game":
            clear_screen()
            recommend_game_random(games)
        elif choice == "Forgotten favorite":
            clear_screen()
            forgotten_favorite(games)
        elif choice == "Search game":
            clear_screen()
            search_game(games)
        elif choice == "Mark as played":
            mark_played(games)

if __name__ == "__main__":
    main()