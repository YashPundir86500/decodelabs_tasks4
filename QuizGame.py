# ============================================================
#          GENERAL KNOWLEDGE QUIZ GAME  🎯
# ============================================================


import random

# ----------------------------------------------------------
# QUESTION BANK (20 questions for better practice)
# Each entry has:
#   "question" : what is asked
#   "answer"   : correct answer in lowercase
#   "correct"  : nicely formatted answer shown on wrong guess
# ----------------------------------------------------------
QUESTION_BANK = [
    # --- Geography ---
    {
        "question": "What is the capital city of France?",
        "answer": "paris",
        "correct": "Paris"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "answer": "pacific",
        "correct": "Pacific Ocean"
    },
    {
        "question": "Which country has the largest area in the world?",
        "answer": "russia",
        "correct": "Russia"
    },
    {
        "question": "What is the capital of Japan?",
        "answer": "tokyo",
        "correct": "Tokyo"
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "answer": "africa",
        "correct": "Africa"
    },

    # --- Science ---
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars",
        "correct": "Mars"
    },
    {
        "question": "What gas do plants absorb during photosynthesis?",
        "answer": "carbon dioxide",
        "correct": "Carbon Dioxide"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "au",
        "correct": "Au"
    },
    {
        "question": "How many bones are in the adult human body?",
        "answer": "206",
        "correct": "206"
    },
    {
        "question": "What is the speed of light (approx) in km/s?",
        "answer": "300000",
        "correct": "300,000 km/s"
    },

    # --- Maths ---
    {
        "question": "How many sides does a hexagon have?",
        "answer": "6",
        "correct": "6"
    },
    {
        "question": "What is the square root of 144?",
        "answer": "12",
        "correct": "12"
    },
    {
        "question": "What is 15% of 200?",
        "answer": "30",
        "correct": "30"
    },

    # --- History ---
    {
        "question": "In which year did World War II end?",
        "answer": "1945",
        "correct": "1945"
    },
    {
        "question": "Who was the first President of the United States?",
        "answer": "george washington",
        "correct": "George Washington"
    },
    {
        "question": "In which year did India gain independence?",
        "answer": "1947",
        "correct": "1947"
    },

    # --- Literature & Arts ---
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "answer": "william shakespeare",
        "correct": "William Shakespeare"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "leonardo da vinci",
        "correct": "Leonardo da Vinci"
    },

    # --- General ---
    {
        "question": "What is the fastest land animal?",
        "answer": "cheetah",
        "correct": "Cheetah"
    },
    {
        "question": "How many colors are there in a rainbow?",
        "answer": "7",
        "correct": "7"
    },
]

# Number of questions asked per round
QUESTIONS_PER_ROUND = 3


# ----------------------------------------------------------
# FUNCTION: Display welcome banner
# ----------------------------------------------------------
def display_banner():
    """Print the welcome banner when the game starts."""
    print("\n" + "=" * 52)
    print("       🎯   GENERAL KNOWLEDGE QUIZ GAME   🎯")
    print("=" * 52)
    print(f"   Answer {QUESTIONS_PER_ROUND} questions per round | 20 in the bank!")
    print("   ✅ +1 for correct  |  ❌ Correct answer shown on wrong")
    print("=" * 52 + "\n")


# ----------------------------------------------------------
# FUNCTION: Final remark based on score
# ----------------------------------------------------------
def get_final_remark(score, total):
    """
    Returns a performance remark based on score.
    Works for any total (not hardcoded to 3).
    """
    if score == total:
        return "🏆 Excellent! Perfect score!"
    elif score == total - 1:
        return "👍 Good Job! Almost perfect!"
    elif score >= total // 2:
        return "😊 Not bad! A little more practice!"
    else:
        return "📚 Keep Practicing! You'll improve!"


# ----------------------------------------------------------
# FUNCTION: Run one full round of the quiz
# ----------------------------------------------------------
def run_quiz(round_number):
    """
    Runs a single quiz round.
    - Randomly picks QUESTIONS_PER_ROUND questions
    - Accepts user input and normalizes it
    - Shows correct answer when user is wrong
    - Returns the score for this round
    """
    print(f"\n{'─' * 52}")
    print(f"  📋 ROUND {round_number}  —  {QUESTIONS_PER_ROUND} Questions")
    print(f"{'─' * 52}\n")

    # Randomly pick questions so every round is different
    selected = random.sample(QUESTION_BANK, QUESTIONS_PER_ROUND)

    score = 0  # Initialize score to 0 at the start of every round

    for index, q in enumerate(selected, start=1):

        # Show question number and question text
        print(f"Q{index}. {q['question']}")

        # Take answer from user — normalize with .strip().lower()
        user_answer = input("   👉 Your answer: ").strip().lower()

        # Use if-else to check the answer
        if user_answer == q["answer"]:
            print("   ✅ Correct!\n")
            score += 1   # Add +1 for every correct answer

        else:
            # Show the correct answer when user gets it wrong (Extra Feature ✅)
            print(f"   ❌ Wrong!")
            print(f"   📌 Correct answer: {q['correct']}\n")

    return score  # Return round score


# ----------------------------------------------------------
# FUNCTION: Display round result
# ----------------------------------------------------------
def display_round_result(score, total, round_number):
    """Show the score and remark after each round."""
    print(f"\n{'─' * 52}")
    print(f"  Round {round_number} Result → Score: {score} / {total}")
    print(f"  {get_final_remark(score, total)}")
    print(f"{'─' * 52}")


# ----------------------------------------------------------
# FUNCTION: Ask if user wants to replay
# ----------------------------------------------------------
def ask_replay():
    """
    Ask the user if they want to play again.
    Loops until a valid answer (yes/no) is entered.
    Returns True to replay, False to quit.
    """
    while True:
        choice = input("\n🔄 Play again? (yes / no): ").strip().lower()
        if choice in ("yes", "y", "haan", "ha"):
            return True
        elif choice in ("no", "n", "nahi", "nope"):
            return False
        else:
            print("   ⚠️  Please type 'yes' or 'no'.")


# ----------------------------------------------------------
# FUNCTION: Show final summary (after all rounds)
# ----------------------------------------------------------
def display_final_summary(all_scores, best_score, total_rounds):
    """
    Show a full summary after the player decides to quit.
    Includes: rounds played, scores per round, best score.
    """
    print("\n" + "=" * 52)
    print("         📊  GAME OVER — FINAL SUMMARY  📊")
    print("=" * 52)
    print(f"  Total rounds played : {total_rounds}")
    print(f"  Questions per round : {QUESTIONS_PER_ROUND}")

    # Show score of each round
    for i, s in enumerate(all_scores, start=1):
        bar = "★" * s + "☆" * (QUESTIONS_PER_ROUND - s)
        print(f"  Round {i}             : {s}/{QUESTIONS_PER_ROUND}  [{bar}]")

    print(f"\n  🥇 Best Score       : {best_score} / {QUESTIONS_PER_ROUND}")
    print("=" * 52)
    print("  👋 Thanks for playing! Keep learning! 🚀")
    print("=" * 52 + "\n")


# ----------------------------------------------------------
# MAIN — Entry point of the game
# Uses a while loop for the replay feature (Extra Feature ✅)
# ----------------------------------------------------------
def main():
    display_banner()

    round_number = 0        # Track which round we're on
    all_scores   = []       # Store score of every round
    best_score   = 0        # Track the highest score

    # ── REPLAY LOOP ── keeps running until user says no
    while True:
        round_number += 1

        # Run the quiz and get the score for this round
        score = run_quiz(round_number)

        # Store and compare scores
        all_scores.append(score)
        if score > best_score:
            best_score = score  # Update best score if this round is better

        # Show result for this round
        display_round_result(score, QUESTIONS_PER_ROUND, round_number)

        # Ask if user wants to play again (Extra Feature ✅)
        if not ask_replay():
            break  # Exit the loop if user says no

    # Show the complete summary after all rounds
    display_final_summary(all_scores, best_score, round_number)


# Run the game only when script is executed directly
if __name__ == "__main__":
    main()