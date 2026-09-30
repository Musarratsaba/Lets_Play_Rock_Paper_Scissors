"""Performance and statistics module."""

from storage import load_rounds
from utils import pause


def show_performance(stats):
    print("\nPERFORMANCE DASHBOARD")
    print("-" * 42)

    total = stats["total_rounds"]
    win_rate = (stats["player_wins"] / total) * 100 if total else 0

    print(f"Games played   : {stats['games_played']}")
    print(f"Rounds played  : {total}")
    print(f"Your wins      : {stats['player_wins']}")
    print(f"Computer wins  : {stats['computer_wins']}")
    print(f"Draws          : {stats['draws']}")
    print(f"Win rate       : {win_rate:.1f}%")

    rounds = load_rounds()
    if rounds:
        print("\nRECENT MOVES")
        for item in rounds[-5:]:
            print(
                f"{item['player'].title():<10} vs "
                f"{item['computer'].title():<10} -> {item['result'].upper()}"
            )

    pause()
