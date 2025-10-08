from dice1 import rollD6, rollD20

num_players = int(input("Enter number of players: "))
wins = [0] * num_players
rounds = 0

while max(wins) < 3:
    rounds += 1
    scores = [rollD6() + rollD20() for _ in range(num_players)]
    print(f"\nRound {rounds}:")
    for i, s in enumerate(scores, 1):
        print(f"Player {i} rolled {s}")

    max_score = max(scores)
    winners = [i for i, s in enumerate(scores) if s == max_score]

    if len(winners) == 1:
        wins[winners[0]] += 1
        print(f"--> Player {winners[0] + 1} wins this round!")
    else:
        print("Tie round!")

champion = wins.index(3) + 1
print(f"\n🏆 Player {champion} is the champion after {rounds} rounds! 🏆")