import json
def display_leaderboard(file_path):
    try:
        with open(file_path, "r") as f:
            scores = json.load(f)
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        top_3 = sorted_scores[:3]
        print("Leaderboard: ")
        for name, score in top_3:
            print(f"{name} : {score}")
    except (FileNotFoundError):
        print("File not found")
    except (json.JSONDecodeError):
        print("No past records present")