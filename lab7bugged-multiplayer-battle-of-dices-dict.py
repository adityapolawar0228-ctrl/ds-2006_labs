#Task15
import random

def rollD6():
    return random.randint(1, 6)

def rollD20():
    return random.randint(1, 20)

# Template dictionary for all players
player_template = {"name": "", "wins": 0}

players = []
num_players = int(input("Enter number of players: "))

# ❌ BUG: appending same dictionary reference each time
for i in range(num_players):
    player = player_template
    player["name"] = input(f"Enter name for Player {i+1}: ")
    players.append(player)

rounds = 5

while max(p["wins"] for p in players) < 3:
    rounds += 1
    print(f"\nRound {rounds}:")
    for p in players:
        score = rollD6() + rollD20()
        p["score"] = score
        print(f"{p['name']} rolled {score}")

    max_score = max(p["score"] for p in players)
    winners = [p for p in players if p["score"] == max_score]

    if len(winners) == 1:
        winners[0]["wins"] += 1
        print(f"--> {winners[0]['name']} wins this round!")
    else:
        print("Tie round!")

champion = max(players, key=lambda x: x["wins"])
print(f"\n🏆 {champion['name']} is the champion after {rounds} rounds! 🏆")
