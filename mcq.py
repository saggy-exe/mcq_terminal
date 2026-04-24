import os
import json


BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "leaderboard.json")


def questions():
    paper = [
    {
        "question" : "Which data structure uses FIFO (First In First Out)?",
        "options" : ["1. Stack","2. Queue","3. Tree","4. Graph",],
        "answer" : 2
    },
    {
        "question" : "What does HTTP stand for?",
        "options" : ["1. Hyper Transfer Text Protocol","2. HyperText Transfer Protocol", "3. HighText Transfer Protocol", "4. HyperText Transmission Process"],
        "answer" : 2
    },
    {
        "question" : "Which of the following is NOT a programming language?",
        "options" : ["1. Python", "2. Java", "3. HTML", "4. C++"],
        "answer" : 3
    },
    {
        "question" : "What is the time complexity of binary search?",
        "options" : ["1. O(n)", "2. O(log n)", "3. O(n²)", "4. O(1)"],
        "answer" : 2
    },
    {
        "question" : "Which component is considered the brain of the computer?",
        "options" : ["1. RAM", "2. Hard Disk", "3. CPU", "4. GPU"],
        "answer" : 3
    },
    {
        "question" : "What does SQL stand for?",
        "options" : ["1. Structured Query Language", "2. Simple Query Language",  "3. Sequential Query Logic", "4. System Query Language"],
        "answer" : 1
    },
    {
        "question" : "Which of these is a NoSQL database?",
        "options" : [ "1. MySQL", "2. PostgreSQL", "3. MongoDB", "4. Oracle"],
        "answer" : 3
    },
    {
        "question" : "In OOP, what does “inheritance” allow?",
        "options" : ["1. Creating multiple objects", "2. Copying code manually", "3. One class to acquire properties of another", "4. Hiding data"],
        "answer" : 3
    },
    {
        "question" : "Which protocol is used to send emails?",
        "options" : ["1. FTP", "2. HTTP", "3. SMTP", "4. TCP"],
        "answer" : 3
    },
    {
        "question" : "What does AI stand for?",
        "options" : ["1. Automated Interface", "2. Artificial Intelligence", "3. Advanced Internet", "4. Algorithmic Input"],
        "answer" : 2
    }]

    return paper


def display_leaderboard():
    try:
        with open(file_path, "r") as f:
            scores = json.load(f)
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        top_3 = sorted_scores[:3]
        print("Leaderboard: ")
        for name, score in top_3:
            print(f"{name} : {score}")
    except (FileNotFoundError,  json.JSONDecodeError):
        print("No past records present")



def start_quiz(paper):
    score = 0
    for i, q in enumerate(paper, start=1):
        question_text = q["question"]           
        print(f"\nQ{i}. {question_text}")
        for option in q["options"]:
            print(option)

        while True:
            try:
                choice = int(input("Enter your answer (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Enter a number.")

        if choice == q["answer"]:
            print("Correct!!")
            score += 1
        else:
            correct = q["options"][q["answer"] - 1]   
            print("Sorry, wrong answer.")
            print(f"Correct answer is : {correct}")

    return score


def main():

    display_leaderboard()
    name = input("Enter your name: ")
    paper = questions()

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
    
    display_leaderboard()


main()

    
