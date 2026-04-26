import json
def display_leaderboard(file_path):
    try:
        with open(file_path, "r") as f:
            scores = json.load(f)
        # sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        scores.sort(
            key=lambda x: (-x["score"], x["timestamp"])
        )

        sorted_scores = scores

        print("Leaderboard: ")
        i=0
        for entry in sorted_scores:
            if i>2:
                break
            print(f"{entry["name"]} scored {entry["score"]}/10 on {entry["timestamp"]}")
            i+=1
            
    except (FileNotFoundError):
        print("File not found")
    except (json.JSONDecodeError):
        print("No past records present")