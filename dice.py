import random

# Wait for the user to press Enter
input("Press Enter to roll the D20...")

# Roll the dice
result = random.randint(1, 20)

# Show the result with D20 info
print("You rolled a D20 and got:", result)
