import random
def CheckIfGreaterThan7(die1, die2):
    return (die1 + die2) > 7
def greet():
    print("What is your name?")
    name = input()
    print(f"Hello, {name}!")
    return name
def roll_two_dices():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)
def main():
    name = greet()
    die1, die2 = roll_two_dices()
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {die1 + die2}")
    if CheckIfGreaterThan7(die1, die2):
        print(f"{name} won!")
    else:
        print(f"{name} lost!")
if __name__ == "__main__":
    main()
