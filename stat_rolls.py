from random import randint
from time import perf_counter

def total_calc():
    total = 0
    while total < dm_total:
        total = 0
        for i in range(6):
            rolls = [randint(1, 6) for _ in range(4)]
            subtotal = sum(rolls) - min(rolls)
            rolls = ", ".join([str(roll) for roll in rolls])
            print(f"\n{subtotal} ({rolls})")
            total += subtotal

        bar = "-" * 62
        print(f"\n{bar}\n")
        print(f"Total: {total}")
        print(f"\n{bar}\n")

if __name__ == "__main__":
    generating = True
    while generating:
        while True: # Checks for valid input so you guys don't crash my program with a single letter
            try:
                dm_total = int(input("What is your DM's total? "))
                break
            except ValueError:
                print("You have not entered a valid number, try again")

        total_calc()

        roll_again = input("Roll again? (y/n): ")
        generating = roll_again.lower().startswith("y")
