import json

def load_json(filename, default):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def update_leaderboard(name, score, distance):
    lb = load_json("leaderboard.json", [])
    lb.append({"name": name, "score": score, "distance": int(distance)})
    lb = sorted(lb, key=lambda x: x['score'], reverse=True)[:10]
    save_json("leaderboard.json", lb)

def get_settings():
    return load_json("settings.json", {"sound": True, "color": "Red", "difficulty": "Medium"})