from random import randint
from time import sleep

def roll_func():
    global add, roll1, roll2, roll3, roll4
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)
    roll4 = randint(1, 6)

    add = roll1 + roll2 + roll3 + roll4

    if roll1 < roll2 or roll1 < roll3 or roll1 < roll4:
        add -= roll1
    elif roll2 < roll1 or roll2 < roll3 or roll2 < roll4:
        add -= roll2
    elif roll3 < roll1 or roll3 < roll2 or roll3 < roll4:
        add -= roll3
    elif roll4 < roll1 or roll4 < roll2 or roll4 < roll3:
        add -= roll4
    elif roll1 == roll2 and roll2 == roll3 and roll3 == roll4:
        add -= roll4

def rig():
    while add < 15:
        roll_func()

    print(f"{roll1}, {roll2}, {roll3}, {roll4}")
    print(f"\n{add}\n")

def rig2():
    while add < 12:
        roll_func()

    print(f"{roll1}, {roll2}, {roll3}, {roll4}")
    print(f"\n{add}\n")

def rig3():
    while add < 7:
        roll_func()

    print(f"{roll1}, {roll2}, {roll3}, {roll4}")
    print(f"\n{add}\n")

if __name__ == "__main__":
    question = input("Rig rolls? (y/n) ")
    if not question.lower().startswith("y"):
        while True:
            for i in range(6):
                roll_func()
                print(f"{roll1}, {roll2}, {roll3}, {roll4}")
                print(f"\n{add}\n")

            roll_again = input("Roll again? (y/n): ")
            if not roll_again.lower().startswith("y"):
                quit()
    else:
        while True:
            for i in range(2):
                roll_func()
                rig()
            for i in range(2):
                roll_func()
                rig2()
            for i in range(2):
                roll_func()
                rig3()

            roll_again = input("Roll again? (y/n): ")
            if not roll_again.lower().startswith("y"):
                quit()