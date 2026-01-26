
#Lab 2: Functions

#Authors: Jacob Miranda
#Group 
#Date: 1/28/2026
#Function: Allows the user to play Rock-Paper-Scissors (RPS) against a computer.
#Takes the user's choice of "weapon" and pits it against the computer's random choice.

import random

#Obtains the user's weapon choice
def weapon_menu():
    print("Please choose your weapon:")
    print("R: Rock")
    print("P: Paper")
    print("S: Scissors")
    print("B: Back")
    weapon_u = input("Enter your choice (R/P/S/B): ").upper()

    #For simplicity, 1 = Rock, 2 = Paper, 3 = Scissors
    if weapon_u == "R":
        return 1
    elif weapon_u == "P":
        return 2
    elif weapon_u == "S":
        return 3
    elif weapon_u == "B":
        return 0
    else:
        print("Invalid choice. Please try again.")
        return weapon_menu()
    
def comp_weapon():
    return random.randint(1, 3)

def main():
    print("Welcome to Rock-Paper-Scissors!")
    playing = True
    while playing():
        print("1. Play game")
        print("2: Show score")
        print("3: Quit")
        play = input()
        if input ==1:
           while True:
            user_weapon = weapon_menu()
            if user_weapon != 0:
                computer_weapon = random.randint(1, 3)
                weapons = {1: "Rock", 2: "Paper", 3: "Scissors"}
                print(f"You chose: {weapons[user_weapon]}") 
                print(f"Computer chose: {weapons[computer_weapon]}")
                break
        elif input == 2:
            print("test")
        elif input == 3:
            playing = False
        else:
            print("Invalid choice. Please try again.")

main()
