# cooler-multiplayer-battle-of-dices-dict.py
import random

num_players = int(input("Enter number of players: "))
players = {}

for i in range(1, num_players+1):
    name = input(f"Enter player {i} name: ")
    players[name] = {"score": 0, "rolls": []}

rounds = int(input("Enter number of rounds: "))

for r in range(rounds):
    print(f"\n--- Round {r+1} ---")
    for player in players:
        roll = random.randint(1, 6)
        players[player]["score"] += roll
        players[player]["rolls"].append(roll)
        print(f"{player} rolled {roll}, total score: {players[player]['score']}")

print("\nFinal Results:")
for player, data in players.items():
    print(f"{player}: {data['score']} points, rolls = {data['rolls']}")

winner = max(players, key=lambda p: players[p]["score"])
print(f"\nWinner: {winner} with {players[winner]['score']} points!")
