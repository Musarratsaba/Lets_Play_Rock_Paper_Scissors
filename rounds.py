"""Saved round browser."""

from storage import load_rounds
from utils import pause


def browse_rounds():
    print("\nSAVED ROUNDS")
    print("-" * 42)

    rounds = load_rounds()
    if not rounds:
        print("No saved rounds yet. Play a game first.")
        pause()
        return

    start = max(0, len(rounds) - 10)
    for index, item in enumerate(rounds[start:], start=start + 1):
        print(
            f"{index:>3}. "
            f"You={item['player'].title():<9} "
            f"Computer={item['computer'].title():<9} "
            f"Result={item['result'].upper()}"
        )

    pause()
