import random
print("\nWelcome to Karl's Python Game\n    Rock, Paper, Scissors.\n\n ")
name = input('Please Enter Name: ')

print('\nWelcome', name)

while True:
    user = input("Make Your Choice (R for ROCK, P for PAPER and S for SCISSORS): ")
    computer = random.randint(1, 3)

    if user == "R":
        print(name, "Selected ROCK")

    if user == "P":
        print(name, "Selected PAPER")

    if user == "S":
        print(name, "Selected SCISSORS")

    if computer == 1:
        computer = "ROCK"
    if computer == 2:
        computer = "PAPER"
    if computer == 3:
        computer = "SCISSORS"

    print(f"\ncomputer selected {computer}.\n")

    if user == computer:
        print(f"Both players Selected {user}. its a Draw!")

    elif user == "R":
        if computer == "SCISSORS":
            print("ROCK smashes SCISSORS!", name, "wins!")
        else:
            print("PAPER covers ROCK!", name, "loses!")

    elif user == "P":
        if computer == "ROCK":
            print("PAPER covers ROCK! ", name, "wins!")
        else:
            print("SCISSORS cuts PAPER! ", name, "loses!")

    elif user == "S":
        if computer == "PAPER":
            print("SCISSORS cuts PAPER! ", name, "wins!")
        else:
            print("ROCK smashes SCISSORS! ", name, " loses!")

    play_again = input("\nPlay again? (Y/N): ")
    if play_again != "Y":
        print("Thank You for Playing My Game ")
        break

