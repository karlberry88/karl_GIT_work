import random

computer_dict = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

num = computer_dict[(random.randint(0, 2))]


def player_rock():
    print("You chose: Rock")
    print()
    print("Computer chose: " + num)
    print()
    if num == "Rock":
        print("It's a tie!")
    elif num == "Paper":
        print("Paper wraps Rock\n --YOU LOSE!--")
    else:
        print("Rock smashes Scissors\n --YOU WIN!--")


def player_paper():
    print("You chose: Paper")
    print()
    print("Computer chose: " + num)
    print()
    if num == "Rock":
        print("Paper wraps Rock\n --YOU WIN!--")
    elif num == "Paper":
        print("It's a tie!")
    else:
        print("Scissors cut Paper\n --YOU LOSE!--")


def player_scissors():
    print("You chose: Scissors")
    print()
    print("Computer chose: " + num)
    print()
    if num == "Rock":
        print("Rock smashes Scissors\n --YOU LOSE!--")
    elif num == "Paper":
        print("Scissors cut Paper\n --YOU WIN!--")
    else:
        print("It's a tie!")


player_choice = input("Rock (R), Paper (P) or Scissors (S)? ")
print()

if player_choice == "R":
    player_rock()
elif player_choice == "P":
    player_paper()
elif player_choice == "S":
    player_scissors()
else:
    print("Invalid entry, try again")