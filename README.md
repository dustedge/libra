# 🎮 Libra

<p align=center><img width="634" height="604" alt="image" src="https://github.com/user-attachments/assets/ea5f3739-046b-4c3e-9909-f008187ca005" /></p>
A terminal-based personal game collection manager. 



## Features

* **Add games** — store name, love score, graphics, gameplay, revisitability, tags, and notes
* **Browse** — scroll through your full collection
* **Search** — fuzzy autocomplete search by game name
* **Recommend** — suggests a game you love (score ≥ 7)
* **Random game** — picks any game at random
* **Forgotten favorite** — surfaces your highest-rated game that you haven't played in the longest time
* **Mark as played** — updates the last-played date to today


## Prerequisites

* **Python 3.8+**

Install dependencies via pip:

```bash
pip install questionary colorama
```

|Package|Purpose|
|-|-|
|`questionary`|Interactive CLI prompts and menus|
|`colorama`|Cross-platform colored terminal output|


## Installation

```bash
git clone https://github.com/dustedge/libra.git
cd game-library
pip install questionary colorama
```


## Usage

Run "Start Libra.lnk" or main.py

or

```bash
python main.py
```

Use arrow keys to navigate the menu and Enter to select. Your game data is saved automatically to `data.json` in the project directory.


## Data Storage

Games are persisted in a local `data.json` file created automatically on first save. No database or external service required.

Each game entry looks like this:

```json
{
  "name": "Hollow Knight",
  "love": 9,
  "graphics": 8,
  "gameplay": 9,
  "revisitability": 3,
  "last_played": "2024-11-02",
  "tags": ["metroidvania", "indie"],
  "notes": "Incredible atmosphere."
}
```

### Field reference

|Field|Type|Description|
|-|-|-|
|`love`|0–10|Overall personal rating|
|`graphics`|0–10|Visual quality|
|`gameplay`|0–10|How fun it is to play|
|`revisitability`|0–3|Never / Rarely / Sometimes / Often|
|`last\_played`|date or null|Date last marked as played|
|`tags`|list|Comma-separated labels|
|`notes`|string|Free-form notes|


## Project Structure

```
game-library/
├── main.py       # Entry point and menu loop
├── actions.py    # All game collection operations
├── storage.py    # JSON read/write
├── utils.py      # Display helpers and input utilities
├── models.py     # Default game structure
└── data.json     # Auto-generated game database
```

