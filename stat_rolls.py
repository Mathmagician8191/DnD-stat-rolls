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

def total_calc():
    global total, final_total
    final_total = 0
    while final_total < dm_total:
        total = []
        for i in range(6):
            roll_func()
            print(f"{roll1}, {roll2}, {roll3}, {roll4}")
            print(f"\n{add}\n")
            total.append(add)

        print("\n--------------------------------------------------------------\n")
        final_total = total[0] + total[1] + total[2] + total[3] + total[4] + total[5]
    print(f"Total: {final_total}")

if __name__ == "__main__":
    while True:
        dm_total = int(input("What is your total? "))
        total_calc()

        roll_again = input("Roll again? (y/n): ")
        if not roll_again.lower().startswith("y"):
            quit()