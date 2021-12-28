import random
SWITCH_CHOICE = True

cars_won = 0
total_turns = 0

for i in range(100_000):  # There will be this many simulated game shows. Default is 100,000. 10,000 is recommended for slow machines.
    possible_prizes = ["car", "goat", "goat"]
    doors = []

    # Pick random door at start
    door_choice = random.randint(0, len(possible_prizes)-1)

    # Randomly place prizes behind each door
    for prize in range(len(possible_prizes)):
        door_prize = random.choice(possible_prizes)
        doors.append(door_prize)
        possible_prizes.remove(door_prize)

    # Reveal goat
    confirmed_goat_door = -1
    for i, prize in enumerate(doors):
        if i != door_choice and prize == "goat":
            confirmed_goat_door = i
            break
    # Check if goat reveal was successful
    # (can fail if there are no other goats to reveal. this can be caused by editing possible_prizes)
    if confirmed_goat_door == -1:
        raise RuntimeError("No suitable goat found to reveal. Increase the amount of goats in possible_prizes.")

    if SWITCH_CHOICE:
        # Find and choose the door that isn't the player's initial choice, and isn't the confirmed goat door
        for i in range(len(doors)):
            if i != door_choice and i != confirmed_goat_door:
                door_choice = i
                break

    # Check if car is behind selected door
    if doors[door_choice] == "car":
        cars_won += 1
    total_turns += 1

if SWITCH_CHOICE:
    print("Strategy: Switch Choice")
else:
    print("Strategy: Stay With Initial Choice")
print(f"Cars: {cars_won}\nTotal Turns: {total_turns}\n≈{round(cars_won / total_turns * 100, 2)}% chance of winning car")
