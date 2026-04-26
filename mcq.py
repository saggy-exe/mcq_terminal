import os
import json
import datetime
from questions import question_list
from quiz_logic import start_quiz
from view_leaderboard import display_leaderboard



def main():

    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "leaderboard.json")


    display_leaderboard(file_path)
    name = input("Enter your name: ")
    paper = question_list()

    score = start_quiz(paper)

    timestamp = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(timestamp, "%d/%m/%Y at %I:%M:%S %p")
    # print(f"Score: {score}/10")
    # print(f"Accuracy: {percentage}%")

    print(f"{name} scored {score}/10 on {timestamp}")

    data = {"name": name, "score": score, "timestamp": timestamp}
    


    try:
        with open(file_path, "r") as f:
            old_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        old_data = []

    old_data.append(data)
    
    with open(file_path, "w") as f:
        json.dump(old_data, f, indent=2)
    
    display_leaderboard(file_path)

if __name__ == "__main__":
    main()

    
