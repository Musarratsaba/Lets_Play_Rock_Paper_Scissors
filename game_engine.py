"""Core Rock Paper Scissors game logic."""

import random
from storage import save_round, save_stats
from utils import CHOICES, choice_name, pause


def get_winner(player, computer):
    if player == computer:
        return "draw"

    winning_pairs = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return "player" if (player, computer) in winning_pairs else "computer"


def ask_choice():
    print("\nChoose your move:")
    print("1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")
    mapping = {"1": "rock", "2": "paper", "3": "scissors"}

    while True:
        value = input("Your choice: ").strip()
        if value in mapping:
            return mapping[value]
        print("Please enter 1, 2, or 3.")


def ask_rounds():
    while True:
        value = input("\nHow many rounds? (1-10): ").strip()
        if value.isdigit() and 1 <= int(value) <= 10:
            return int(value)
        print("Enter a whole number from 1 to 10.")


def play_game(stats):
    print("\nSTART A NEW GAME")
    print("-" * 42)
    rounds = ask_rounds()

    player_score = 0
    computer_score = 0
    draws = 0

    for number in range(1, rounds + 1):
        print(f"\n--- ROUND {number}/{rounds} ---")
        player = ask_choice()
        computer = random.choice(CHOICES)
        result = get_winner(player, computer)

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            draws += 1

        stats["total_rounds"] += 1
        stats["player_wins"] += result == "player"
        stats["computer_wins"] += result == "computer"
        stats["draws"] += result == "draw"

        save_round({
            "round": number,
            "player": player,
            "computer": computer,
            "result": result,
        })

        print(f"You: {choice_name(player)}")
        print(f"Computer: {choice_name(computer)}")
        print(f"Result: {result.upper()}")

    stats["games_played"] += 1
    save_stats(stats)

    print("\n" + "=" * 42)
    print("GAME RESULT")
    print("=" * 42)
    print(f"You: {player_score} | Computer: {computer_score} | Draws: {draws}")

    if player_score > computer_score:
        print("🏆 You won the game!")
    elif computer_score > player_score:
        print("🤖 Computer won the game.")
    else:
        print("🤝 The game ended in a draw.")

    pause()
