

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


if __name__ == "__main__":
    start_quiz()