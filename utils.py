"""User-interface helpers and shared constants."""

import os

CHOICES = ("rock", "paper", "scissors")

ICONS = {
    "rock": "🪨 Rock",
    "paper": "📄 Paper",
    "scissors": "✂️ Scissors",
}


def choice_name(value):
    return ICONS.get(value, value.title())


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def print_banner():
    print("╔══════════════════════════════════════════╗")
    print("║     LET'S PLAY: ROCK PAPER SCISSORS      ║")
    print("║        choose a mode and play!           ║")
    print("╠══════════════════════════════════════════╣")


def print_menu():
    print("║              GAME HUB                    ║")
    print("║                                          ║")
    print("║  1  Start a new game                     ║")
    print("║  2  View performance                     ║")
    print("║  3  Browse saved rounds                  ║")
    print("║  4  How to play                          ║")
    print("║  5  Exit the game                        ║")
    print("╚══════════════════════════════════════════╝")
