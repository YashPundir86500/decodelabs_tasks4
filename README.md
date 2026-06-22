# 🎯 General Knowledge Quiz Game

A fun and interactive command-line quiz game built in Python. Test your knowledge across Geography, Science, Mathematics, History, and Literature — with a replay feature and round-wise score tracking!

---

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Question Categories](#question-categories)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [Author](#author)

---

## ✨ Features

- 🧠 **20-question bank** covering 5 categories
- 🔀 **Random question selection** — every round is unique
- 🔁 **Replay system** — play as many rounds as you want
- 📊 **Round-wise score tracking** with star ratings
- 🏆 **Best score tracking** across all rounds
- 📌 **Correct answer revealed** on wrong guess
- 📋 **Final summary** with complete stats after the game ends
- 🌍 Accepts **regional language inputs** for yes/no (`haan`, `nahi`, etc.)

---

## 🎮 Demo

```
====================================================
       🎯   GENERAL KNOWLEDGE QUIZ GAME   🎯
====================================================
   Answer 3 questions per round | 20 in the bank!
   ✅ +1 for correct  |  ❌ Correct answer shown on wrong
====================================================

Q1. Which planet is known as the Red Planet?
   👉 Your answer: mars
   ✅ Correct!

Q2. Who painted the Mona Lisa?
   👉 Your answer: picasso
   ❌ Wrong!
   📌 Correct answer: Leonardo da Vinci
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- No external libraries required — uses only the Python standard library

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/quiz-game.git

# Navigate into the project folder
cd quiz-game
```

### Run the Game

```bash
python QuizGame.py
```

---

## 🕹️ How to Play

1. Run the script using the command above.
2. Answer each question by typing your response and pressing **Enter**.
3. You will be shown the correct answer if you get one wrong.
4. After each round, your score is displayed.
5. Choose to **play again** or **quit** — a full summary is shown at the end.

**Accepted inputs for replay prompt:**

| Play Again | Quit      |
|------------|-----------|
| `yes`, `y` | `no`, `n` |
| `haan`, `ha` | `nahi`, `nope` |

---

## 📁 Project Structure

```
quiz-game/
│
├── QuizGame.py        # Main game file
└── README.md          # Project documentation
```

### Key Functions

| Function | Description |
|---|---|
| `display_banner()` | Shows the welcome screen |
| `run_quiz(round_number)` | Runs one complete quiz round |
| `get_final_remark(score, total)` | Returns performance feedback |
| `display_round_result(...)` | Shows score after each round |
| `ask_replay()` | Prompts user to replay or quit |
| `display_final_summary(...)` | Shows complete game stats |
| `main()` | Entry point — manages the game loop |

---

## 📚 Question Categories

| Category | No. of Questions |
|----------|-----------------|
| 🌍 Geography | 5 |
| 🔬 Science | 5 |
| ➕ Mathematics | 3 |
| 📜 History | 3 |
| 🎨 Literature & Arts | 2 |
| 🌐 General | 2 |
| **Total** | **20** |

---

## ⚙️ Configuration

You can easily customize the game by editing these constants at the top of `QuizGame.py`:

```python
# Number of questions asked per round (default: 3)
QUESTIONS_PER_ROUND = 3
```

To **add new questions**, append an entry to the `QUESTION_BANK` list:

```python
{
    "question": "Your question here?",
    "answer": "correct answer in lowercase",
    "correct": "Nicely Formatted Answer"
}
```

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Module:** `random` (standard library)
- **Interface:** Command Line (CLI)

---

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
