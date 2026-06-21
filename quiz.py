import json
import random
import time
with open("questions.json") as f:
    questions = json.load(f)

# Prints the rules in the starting menu
def rules():
    print(f"\033[40m\n{' Multiple Choice Quiz '.center(100, '=')}\nRules: ANSWER ALL 10 QUESTIONS\n       NO CHEATING\n       QUIZ IS TIMED\n       TYPE ANSWER AS SHOWN\n       HAVE FUN\n{'='*100}\033[0m")
    print("""
    1. Start game
    2. Leaderboard
    3. Quit
    """)

# Decision made from starting menu
def path_chosen():
    while True:
        selection = input("Enter your choice: ")
        if selection in ["1", "2", "3"]: 
            break
        print("Please enter 1, 2, or 3")
    return selection

# Starts game and adds name + score to leaderboard, makes changes to top 10 scores
def start_game():
    start_time = time.time()
    random.shuffle(questions)
    score = 0
    for q in questions:
        correct = q["answer"]
        print("\n"+q["question"])
        for i, each in enumerate(q["choices"]):
            print(chr(i+65) + ")", each)
        while True:
            user_answer = input("Answer: ")
            if user_answer in ["A", "B", "C", "D"]: 
                break
            print("Please enter A, B, C, or D") 
        if user_answer == correct:
            print("Correct!")
            input("Press Enter to continue...")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {correct}")
            input("Press Enter to continue...")
# Timing calculations and scale
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time <= 5:
        time_score = 1.00
    elif elapsed_time >= 120:
        time_score = 0.01
    else:
        time_score = round(1.00 + (elapsed_time - 5) * (0.01 - 1.00) / (120 - 5), 3)
# Score and leaderboard
    # Score from just the quiz scaled
    quiz_score = score * 0.1
    # Weighted score based on quiz and time
    weighted_score = round(0.75 * quiz_score + 0.25 * time_score, 3)
    if score == 10:
        print(f"\nPerfect! Your score is {score}")
    elif score >= 7:
        print(f"Great Job! Your score is {score}")
    elif score >= 4:
        print(f"Try Harder! Your score is {score}")
    else:
        print(f"You need to study! Your score is {score}")
    name = input("Enter your name: ")
    try:
        with open("leaderboard.json") as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = []
    leaderboard.append({"name": name, "score": score, "time": elapsed_time, "weighted_score": weighted_score})
    leaderboard.sort(key=lambda entry: entry["weighted_score"], reverse=True)
    top_ten = leaderboard[:10]
    with open("leaderboard.json", "w") as f:
        json.dump(top_ten, f)
    main()

# Menu selection on the leaderboard screen
def leaderboard_menu():
    print("""
    1. Back to menu
    2. Quit
    """)
    while True:
        selection = input("Enter your choice: ")
        if selection in ["1", "2"]:
            break
        print("Please enter 1 or 2")
    return selection

# The main function which displays the rules and decides what is done based off selection
def main():
    rules()
    selection = path_chosen()
    if selection == "1":
        start_game()
    elif selection == "2":
        show_leaderboard()
    else:
        quit()

# Shows the leaderboard with top 10 scores
def show_leaderboard():
    try:
        with open("leaderboard.json") as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = []
    print("="*100)
    print("Top Scores All Time".center(100, ' '))
    print("="*100)
    print(f"\033[4m{'Name':<15}{'Score':<15}{'Time':<10}\033[0m")
    for data in leaderboard:
        print(f"{data['name']:<15}{data['score']:<15}{round(data['time'], 2):<10}")
    selection = leaderboard_menu()
    if selection == "1":
        main()
    else:
        quit()

main()