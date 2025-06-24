import random
# import matplotlib.pyplot as plt  
# # Optional: for graphing results

# Welcome Message
print("🎲 Welcome to the Dice Roll Simulator!")

rolls = []  # List to store all dice rolls

while True: # infinite loop
    input("Press Enter to roll the dice... ")

    # Simulate rolling a 6-sided dice
    dice = random.randint(1, 6)
    rolls.append(dice)
    print(f"You rolled a {dice} 🎉")

    cont = input("Roll again? (y/n): ").lower()
    if cont != "y":
        break

# After the loop: show summary and plot
print("\nThanks for playing! Here's your dice roll summary:")
for i in range(1, 7):
    print(f"{i}: {rolls.count(i)} times")

# Bar chart of results
try:
    import matplotlib.pyplot as plt


    plt.hist(rolls, bins=range(1, 8), edgecolor='black', align='left')
    plt.title('Dice Roll Distribution')
    plt.xlabel('Dice Number')
    plt.ylabel('Frequency')
    plt.xticks(range(1, 7))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
except ImportError:
    print("\nMatplotlib not installed. Skipping graph. To enable it, run:")
    print("pip install matplotlib")