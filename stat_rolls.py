from random import randint

def roll_func():
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)
    roll4 = randint(1, 6)

    l = (roll1, roll2, roll3, roll4)

    X = l.index(min(l))

    add = roll1 + roll2 + roll3 + roll4 - l[X]

    return add, roll1, roll2, roll3, roll4

def total_calc():
    final_total = 0
    while final_total < dm_total:
        total = []
        for i in range(6):
            add, roll1, roll2, roll3, roll4 = roll_func()
            print(f"{roll1}, {roll2}, {roll3}, {roll4}")
            print(f"\n{add}\n")
            total.append(add)

        print("--------------------------------------------------------------\n")
        final_total = total[0] + total[1] + total[2] + total[3] + total[4] + total[5]
        print(f"Total: {final_total}\n")
        print("--------------------------------------------------------------\n")

if __name__ == "__main__":
    while True: # Loops entire program
        while True: # Checks for valid input so you guys don't crash my program with a single letter
            try:
                dm_total = int(input("What is your DM's total? "))
                break
            except ValueError:
                print("You have not entered a valid number, try again")

        total_calc()

        roll_again = input("Roll again? (y/n): ")
        if not roll_again.lower().startswith("y"):
            quit()
