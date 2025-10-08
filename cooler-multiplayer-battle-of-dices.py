# cooler-multiplayer-battle-of-dices.py
from dice1 import rollD6, rollD20

def play_round(num_players):
    scores = [rollD6() + rollD20() for _ in range(num_players)]
    for i, s in enumerate(scores, 1):
        print(f"Player {i}: {s}")
    return scores

def get_round_winner(scores):
    max_score = max(scores)
    winners = [i for i, s in enumerate(scores) if s == max_score]
    return winners if len(winners) == 1 else None

def play_game(num_players):
    wins = [0] * num_players
    rounds = 0
    while max(wins) < 3:
        rounds += 1
        print(f"\n--- Round {rounds} ---")
        scores = play_round(num_players)
        winner = get_round_winner(scores)
        if winner:
            wins[winner[0]] += 1
            print(f"🎉 Player {winner[0] + 1} wins the round!")
        else:
            print("🤝 Tie round!")
    champion = wins.index(3) + 1
    print(f"\n🔥 Player {champion} is the champion in {rounds} rounds! 🔥")

num_players = int(input("Enter number of players: "))
play_game(num_players)
