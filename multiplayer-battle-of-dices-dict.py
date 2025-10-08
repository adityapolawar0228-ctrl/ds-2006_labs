# multiplayer-battle-of-dices-dict.py
import random

num_players = int(input("Enter number of players: "))
players = {}

for i in range(1, num_players+1):
    name = input(f"Enter player {i} name: ")
    players[name] = {"score": 0}

rounds = int(input("Enter number of rounds: "))

for r in range(rounds):
    print(f"\n--- Round {r+1} ---")
    for player in players:
        roll = random.randint(1, 6)
        players[player]["score"] += roll
        print(f"{player} rolled {roll}, total score: {players[player]['score']}")

winner = max(players, key=lambda p: players[p]["score"])
print(f"\nWinner: {winner} with {players[winner]['score']} points!")
