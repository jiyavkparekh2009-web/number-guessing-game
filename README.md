# Number Guessing Game

A Python-based Number Guessing Game where the player has three attempts to guess a randomly generated number between 1 and 100.

## Features

- Generates a random number between 1 and 100
- Allows a maximum of 3 attempts
- Provides hints when the guess is too high or too low
- Displays a success message when the correct number is guessed
- Shows the total number of attempts used
- Beginner-friendly command-line project

## Concepts Used

- Python Variables
- User Input
- Conditional Statements (`if`, `elif`)
- While Loops
- Random Module
- Basic Game Logic

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python number_guessing_game.py
```

## Game Rules

- The computer generates a random number between 1 and 100.
- You have only 3 attempts to guess the correct number.
- After each incorrect guess, a hint is provided:
  - "Too High!"
  - "Too Low!"
- If the correct number is guessed within 3 attempts, you win.
- Otherwise, the game ends and you lose.

## Sample Output

```text
========================================

Number Guessing Game

========================================

You will get only 3 attempts

Enter the number : 50
Too Low!

Enter the number again : 75
Too High!

Enter the number again : 68
Congratulations! You guessed the correct number.

Total Attempts: 3
```

## Author

Jiya Parekh

## License

This project is licensed under the MIT License.
