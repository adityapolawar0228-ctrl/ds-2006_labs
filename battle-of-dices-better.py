# task13.py
from dice1 import rollD6

p1_wins = 0
p2_wins = 0
rounds = 0

while p1_wins < 3 and p2_wins < 3:
    rounds += 1
    p1 = rollD6()
    p2 = rollD6()
    print(f"Round {rounds}: {p1} vs {p2}")

    if p1 > p2: p1_wins += 1
    elif p2 > p1: p2_wins += 1

print("Winner decided in", rounds, "rounds")



