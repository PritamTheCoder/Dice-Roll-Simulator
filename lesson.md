
# 🎲 Beginner Python Project: Dice Roll Simulator

Welcome to your **first hands-on Python project**!

In this lesson, you'll build a fun and simple Dice Roll Simulator while learning key Python concepts. You'll simulate a dice roll, keep track of results, and optionally visualize the data with a chart.

---

## 🎯 What You'll Build

A Python program that:
- Simulates rolling a 6-sided dice.
- Repeats as long as the user wants.
- Stores each roll in a list.
- Shows a summary of all rolls.
- (Optional) Displays a chart of roll frequencies using `matplotlib`.

---

## 🧠 Concepts You'll Learn

| Python Concept        | What It Means |
|------------------------|----------------|
| `print()`              | Display messages to the screen |
| `input()`              | Take user input |
| `while` loop           | Repeat code until a condition is false |
| `random.randint()`     | Generate random numbers |
| `lists` (`[]`)         | Store multiple values |
| `.append()`            | Add values to a list |
| `.count()`             | Count specific values in a list |
| `matplotlib.pyplot`    | (Optional) Create data visualizations |

---

## 🛠️ Step-by-Step Instructions

### 🔹 Step 1: Set Up Your Environment

Make sure Python 3 is installed:
```bash
python --version
```

Create a project folder:
```
dice-roll-simulator/
```

Inside it, create a Python file:
```
dice_simulator.py
```

---

### 🔹 Step 2: Print a Welcome Message

```python
print("🎲 Welcome to the Dice Roll Simulator!")
```

Run your file:
```bash
python dice_simulator.py
```

---

### 🔹 Step 3: Import the Random Module

```python
import random
```

This gives access to the `random.randint()` function, which simulates a dice roll.

---

### 🔹 Step 4: Simulate Dice Rolls in a Loop

```python
rolls = []  # List to store results

while True:
    input("Press Enter to roll the dice... ")
    dice = random.randint(1, 6)
    rolls.append(dice)
    print(f"You rolled a {dice} 🎉")

    cont = input("Roll again? (y/n): ").lower()
    if cont != 'y':
        break
```

✅ What’s happening here:
- We wait for the user to press Enter.
- A random number (1–6) is generated.
- It’s saved in the `rolls` list.
- The user is asked if they want to roll again.

---

### 🔹 Step 5: Show a Summary of Rolls

```python
print("\nThanks for playing! Here's your dice roll summary:")

for i in range(1, 7):
    print(f"{i}: {rolls.count(i)} times")
```

✅ This prints how many times each dice number was rolled using `.count()`.

---

### 🔹 Step 6 (Optional): Plot the Results

Install `matplotlib` first (once):
```bash
pip install matplotlib
```

Then add this to the end of your Python file:

```python
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
    print("\nmatplotlib not installed. Skipping graph.")
```

---

## 📁 Final Folder Structure

```
dice-roll-simulator/
├── dice_simulator.py
├── plot.png            # Optional chart screenshot
├── README.md
├── lesson.md
├── requirements.txt
└── .gitignore
```

---

## 📦 requirements.txt

If you use the chart, add this file:
```
matplotlib
```

---

## ✅ Summary of What You Learned

- Basic Python syntax (`print`, `input`, `while`, `for`)
- Generating random values
- Storing and analyzing data using lists
- Optional data visualization with `matplotlib`

---

## 🚀 Next Steps

Here are ideas to level up:
- 🎲 Simulate **two** dice and show totals
- 🧱 Create a GUI using `Tkinter`
- 🌐 Deploy your project with `Flask` on Render
- 📊 Analyze other experiments (coin flips, card draws)

---

## 🙌 Final Thoughts

You've just completed your first real Python project!

You built a working app that:
- Interacts with the user
- Stores and processes data
- Optionally visualizes the result

🎉 **Upload it to GitHub** and show it off!

---
