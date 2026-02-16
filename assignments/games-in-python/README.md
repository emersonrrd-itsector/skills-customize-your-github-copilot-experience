
```markdown

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python that exercises string manipulation, loops, conditionals, and basic user I/O.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a playable Hangman game that randomly selects a secret word and lets the player guess letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list (see `starter-code.py`).
- Prompt the player to guess single letters and update the displayed word progress (e.g. `_ p p _ e`).
- Track and display letters already guessed and the number of incorrect guesses remaining.
- End the game when the player guesses the full word or reaches the maximum number of incorrect guesses.
- Print a clear win or lose message showing the secret word.

## 🧰 Starter Files

- `starter-code.py` — minimal scaffold with word list and TODOs.

## ▶️ How to run

Run the starter script with Python 3:

```bash
python3 starter-code.py
```

## 💡 Hints

- Use `random.choice()` to pick the secret word.
- Keep a set/list of guessed letters and validate input (single alphabetical character).
- Build a helper to render the current progress string from the secret word and guessed letters.

## 🚀 Stretch Goals

- Load words from an external file (`words.txt`).
- Add difficulty levels that change `max_incorrect`.
- Support full-word guesses.

## 🎓 Learning Outcomes

- Practice working with strings, lists/sets, loops, and conditionals.
- Learn to design a simple game loop and manage program state.

## 📬 Submission

Commit your completed `starter-code.py` changes to this assignment folder and open a PR when ready.

```
