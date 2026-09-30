"""JSON storage layer for statistics and saved rounds."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
STATS_FILE = DATA_DIR / "stats.json"
ROUNDS_FILE = DATA_DIR / "rounds.json"

DEFAULT_STATS = {
    "games_played": 0,
    "total_rounds": 0,
    "player_wins": 0,
    "computer_wins": 0,
    "draws": 0,
}


def _ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)


def _read_json(path, default):
    _ensure_data_dir()
    if not path.exists():
        return default.copy() if isinstance(default, dict) else list(default)

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return default.copy() if isinstance(default, dict) else list(default)


def _write_json(path, data):
    _ensure_data_dir()
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_stats():
    stats = _read_json(STATS_FILE, DEFAULT_STATS)
    for key, value in DEFAULT_STATS.items():
        stats.setdefault(key, value)
    return stats


def save_stats(stats):
    _write_json(STATS_FILE, stats)


def load_rounds():
    return _read_json(ROUNDS_FILE, [])


def save_round(round_data):
    rounds = load_rounds()
    rounds.append(round_data)
    _write_json(ROUNDS_FILE, rounds)
