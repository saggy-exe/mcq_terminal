import os
import json
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
    percentage = score * 10
    print(f"Score: {score}/10")
    print(f"Accuracy: {percentage}%")

    data = {name: score}
    


    old_data = dict()
    try:
        with open(file_path, "r") as f:
            old_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        old_data = {}

    new_data = old_data | data
    
    with open(file_path, "w") as f:
        json.dump(new_data, f, indent=2)
    
    display_leaderboard(file_path)

if __name__ == "__main__":
    main()

    
