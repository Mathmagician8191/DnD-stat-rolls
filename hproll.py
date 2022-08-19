from random import randint

while True:
    hit_die = int(input("What's your hit die? "))

    con_mod = int(input("What's your constitution modifier? "))

    hp_roll = randint(1,hit_die)

    avg_hp = (hit_die / 2) + 1

    max_hp = hit_die + con_mod

    print(f"Max HP: {max_hp}")
    print(f"Average HP (from hit dice max): {avg_hp}")
    print(f"Average HP with constitution modifier: " + str(avg_hp + con_mod))
    print(f"Base HP roll: {hp_roll}")
    print("Roll with constitution modifier: " + str(hp_roll + con_mod))

    roll_again = input("Roll again? (y/n) ")
    if not roll_again.lower().startswith("y"):
        quit()