import random as rd

possible_actions = ["rock", "paper", "scissors"]

x = 1

while x <= 3:
    computer_action = rd.choice(possible_actions)
    action = input("Enter a choice (rock, paper, scissors): ")
    print(f"\nYou chose {action}, computer chose {computer_action}.")

    if action == computer_action:
        print(f"Both Players selected {action}, it's a tie!")
        x = 0
    elif action == "rock":
        if computer_action == 'scissors':
            print(f"Other player chose {computer_action}, you win!!!")
            x += 1
        else: 
            print(f"Other player chose {computer_action}, you Lose!")
    elif action == "paper":
        if computer_action == 'rock':
            print(f"Other player chose {computer_action}, you win!!!")
            x += 1
        else: 
            print(f"Other player chose {computer_action}, you Lose!")
    elif action == "scissors":
        if computer_action == 'paper':
            print(f"Other player chose {computer_action}, you win!!!")
            x += 1
        else: 
            print(f"Other player chose {computer_action}, you Lose!")

    if x == 3:
        print("You have won 3 in a row! Game over.")
        break