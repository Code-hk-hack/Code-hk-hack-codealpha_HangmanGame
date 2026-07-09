# 🎮 Hangman Game

A classic console-based Hangman game. The program randomly selects a secret word, and the player has 6 incorrect guesses to figure it out one letter at a time.

## Features
- Random word selection from a predefined word bank
- Tracks guessed letters to prevent repeat guesses
- Input validation (rejects anything that isn't a single alphabet letter)
- Displays remaining incorrect guesses and progress after each turn
- Win/loss detection with a final reveal of the secret word

## Concepts Demonstrated
- Functions (`play_hangman()`)
- Lists and sets
- The `random` module
- `while` loops with compound conditions
- `if / else` logic for input validation and win/loss checks
- String and list manipulation (`enumerate`, `.join()`)

## How to Run
```bash
python Hangman_Game.py
```

## Example Interaction
```
=== Welcome to Hangman! ===
The word has 6 letters.

_ _ _ _ _ _
Incorrect guesses remaining: 6
Guessed letters: None
Guess a letter: p
✅ Good job! 'p' is in the word.
```

## Possible Improvements
- Add difficulty levels with longer/shorter word banks
- Display an ASCII hangman figure that updates with each wrong guess
- Let the player choose a category (animals, countries, etc.)
