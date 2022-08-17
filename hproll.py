from random import randint

while True:
    hit_die = int(input("What's your hit die? "))

    hp_roll = randint(1,hit_die)

    print(hp_roll)

    roll_again = input("Roll again? (y/n) ")
    if not roll_again.lower().startswith("y"):
        quit()