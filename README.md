# 🎮 Mystery Guessing Game 🚀

Welcome to my **Number Guessing Game**! This project started as a simple Python tutorial from GeeksforGeeks and evolved into a fully interactive desktop app with custom photos, sound effects, and a "squeezing" hint system.



[Image of binary search algorithm flowchart]


## ✨ Features
* **Smart Math:** Uses a Binary Search algorithm to calculate exactly how many chances you need to find the number fairly.
* **Mystery Range:** The computer picks a random starting and ending number every time you play.
* **3 Squeezing Hints:** * **Hint 1:** Narrows the range to 50 numbers.
    * **Hint 2:** Narrows the range to 30 numbers.
    * **Hint 3:** Narrows the range to only 15 numbers!
* **Personalization:** Users can upload their own background photos directly from their computer.
* **Sound Effects:** Plays a "Win" sound when you guess correctly.

## 🛠️ How It Works (The Algorithm)
This game is based on the logic of **Binary Search**:
1.  **Input:** The user defines a range or the computer picks one.
2.  **Randomization:** A secret integer is selected within that interval.
3.  **Calculation:** The maximum allowed guesses are calculated using the formula: $$log_2(Upper - Lower + 1)$$
4.  **Feedback:** The game tells you if your guess is "Too High" or "Too Low" to help you refine your next attempt.

## 🚀 How to Play
1.  **Download** the `main.py` and `win.wav` files.
2.  **Run** the game in your terminal: `python main.py`
3.  **Guess** the number before you run out of chances!
4.  **Hint:** Use your 3 hints wisely when you get stuck!

## 📸 Screenshots
*(Tip: Add a screenshot of your working game here!)*


## 🏆 Hall of Fame (Leaderboard)

| Rank | Player Name | Max Level | High Score |
| :--- | :--- | :--- | :--- |
| 1 | CodingHero2026 | Level 12 | 4,500 |
| 2 | SuperCoder11 | Level 8 | 2,800 |
| 3 | PythonMaster | Level 5 | 1,200 |

*To get on the leaderboard, send me a screenshot of your game over screen!*

---
Built with ❤️ by an 11-year-old developer using Python and Tkinter.
