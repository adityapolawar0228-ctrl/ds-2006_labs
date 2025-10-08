# task14.py
from dice1 import rollD6, rollD20

p1_wins = 0
p2_wins = 0
rounds = 0

while p1_wins < 3 and p2_wins < 3:
    rounds += 1
    p1 = rollD6() + rollD20()
    p2 = rollD6() + rollD20()
    print(f"Round {rounds}: Player1={p1}, Player2={p2}")

    if p1 > p2: p1_wins += 1
    elif p2 > p1: p2_wins += 1
    else: print("Tie round!")

if p1_wins == 3:
    print("🔥 Player 1 is the champion in", rounds, "rounds! 🔥")
else:
    print("⚡ Player 2 is the champion in", rounds, "rounds! ⚡")
