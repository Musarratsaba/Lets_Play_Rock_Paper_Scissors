# LET'S PLAY: ROCK PAPER SCISSORS

A menu-driven command-line Rock Paper Scissors game built in Python for the VITyarthi Python Essentials evaluated project.

## Overview

The project turns the classic game into a small personal game hub. A user can start a new multi-round game, view performance statistics, browse saved rounds, read the rules, and exit.

The project uses only Python's standard library, so no external package installation is required.

## Features

1. Start a new game with 1-10 rounds.
2. Computer chooses a move randomly.
3. Automatic winner calculation.
4. Game score and final result.
5. Persistent statistics stored in JSON.
6. Saved round history.
7. Performance dashboard with win rate.
8. Input validation and error handling.
9. Unit tests for the core game logic.
10. Clean modular file structure.

## Project Structure

```text
RockPaperScissors_VITyarthi/
├── main.py
├── game_engine.py
├── performance.py
├── rounds.py
├── storage.py
├── utils.py
├── config.py
├── README.md
├── statement.md
├── requirements.txt
├── Project_Report.pdf
├── data/
│   ├── stats.json
│   └── rounds.json
├── tests/
│   └── test_game_engine.py
└── docs/
    ├── architecture.md
    ├── workflow.md
    ├── design_notes.md
    └── uml.md
```

## Requirements

- Python 3.9 or newer
- Command-line terminal
- No external Python packages

## Installation

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Check Python:

```bash
python --version
```

4. No `pip install` step is required because the project uses the standard library.

## Run

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

## Testing

```bash
python -m unittest discover -s tests -v
```

## Data

The application creates/updates `data/stats.json` and `data/rounds.json` automatically.

## Main Modules

- `main.py` - menu and application workflow.
- `game_engine.py` - game rules and scoring.
- `performance.py` - statistics dashboard.
- `rounds.py` - saved-round browser.
- `storage.py` - JSON read/write operations.
- `utils.py` - shared UI helpers and constants.
- `config.py` - configuration values.

## Future Enhancements

- Two-player local mode.
- Difficulty levels.
- Tournament mode.
- Leaderboard.
- CSV export.
- Graphical interface.
- Sound effects.
