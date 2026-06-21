Quiz Game

A command-line multiple choice quiz game written in Python. Questions are loaded from a JSON file, scores are ranked on a persistent leaderboard, and rankings are weighted by both accuracy and speed.

Features:

Multiple choice quiz with randomized question order
Input validation on every prompt (menu choices and answers)
Persistent leaderboard saved between runs using JSON
Top 10 scores only — the leaderboard automatically trims itself
Score is timed and combined with accuracy into a single ranking

How to play:

Make sure you have Python 3 installed
Clone this repository
Run the game from the project folder:

bash   python quiz.py

Follow the on-screen menu to start a game, view the leaderboard, or quit

How scoring works:

Each finished game produces a score out of 10 and a total time. To rank the leaderboard fairly, both are blended into a single weighted score:

Accuracy (75% of the weight): raw score out of 10, scaled to a 0–1 range
Speed (25% of the weight): total time to answer all questions, scaled so 5 seconds or faster earns the maximum speed score and 2 minutes or slower earns the minimum

The two are combined into one weighted_score used purely for ranking. The leaderboard itself still displays the raw score and time, not the formula, so it stays easy to read.

Project structure

quiz_game/
├── quiz.py            # Game logic
├── questions.json     # Question bank
├── leaderboard.json   # Saved scores (created automatically, not tracked in git)
└── .gitignore

Adding your own questions

Open questions.json and add new entries following this format:

json{
  "category": "Science",
  "question": "What planet is closest to the Sun?",
  "choices": ["Venus", "Mercury", "Earth", "Mars"],
  "answer": "Mercury"
}

About

Built as a learning project to practice file I/O, JSON handling, functions, input validation, sorting with custom keys, and basic data persistence in Python.
