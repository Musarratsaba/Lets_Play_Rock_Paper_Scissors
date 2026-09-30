"""Entry point for the Rock Paper Scissors project."""

from game_engine import play_game
from performance import show_performance
from rounds import browse_rounds
from storage import load_stats
from utils import clear_screen, pause, print_banner, print_menu


def how_to_play():
    clear_screen()
    print_banner()
    print("\nHOW TO PLAY")
    print("-" * 42)
    print("Rock beats Scissors.")
    print("Scissors beats Paper.")
    print("Paper beats Rock.")
    print("Choose 1, 2, or 3 during a game.")
    print("You can play single or multi-round games.")
    print("Your results are saved automatically.")
    pause()


def main():
    stats = load_stats()

    while True:
        clear_screen()
        print_banner()
        print_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            play_game(stats)
        elif choice == "2":
            show_performance(stats)
        elif choice == "3":
            browse_rounds()
        elif choice == "4":
            how_to_play()
        elif choice == "5":
            clear_screen()
            print("\nThanks for playing! 👋")
            break
        else:
            print("\nInvalid choice. Please enter 1-5.")
            pause()


if __name__ == "__main__":
    main()
