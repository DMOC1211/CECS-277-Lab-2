#Lab 2: Functions

#Authors: Jacob Miranda & Daniel Puerto
#Group: 11 
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

    #For simplicity, returns a number value. 1 = Rock, 2 = Paper, 3 = Scissors
    if weapon_u == "R":
        print("You chose Rock")
        return 1
    elif weapon_u == "P":
        print("You chose Paper")
        return 2
    elif weapon_u == "S":
        print("You chose Scissors")
        return 3
    elif weapon_u == "B":
        return 0
    else:
        print("Invalid choice. Please try again.")
        return weapon_menu()
    
#Gives the computer a random number coresponding to a weapon. Prints choice then returns the numerical value
def comp_weapon():
    comp_weap = random.randint(1, 3)
    if comp_weap == 1:
        print("Computer chose Rock")
    elif comp_weap == 2:
        print("Computer chose Paper")
    elif comp_weap == 3:
        print("Computer chose Scissors")
    return comp_weap

#finds the winner based on hard-coded matchups. Returns 0 for tie, 1 for player win, 2 for computer
def find_winner(p_wep, c_wep): 

    if p_wep == c_wep:
        print("It's a tie!")
        return 0
    if p_wep == 1 and c_wep == 3:
        print("Player wins")
        return 1
    if p_wep == 1 and c_wep == 2 :
        print("Computer wins")
        return 2
    if p_wep == 3 and c_wep == 1 :
        print("Computer wins")
        return 2
    if p_wep == 3 and c_wep == 2:
        print("Player wins")
        return 1
    if p_wep == 2 and c_wep == 1:
        print("Player wins")
        return 1
    if p_wep == 2 and c_wep == 3:
        print("Computer wins")
        return 2


#Function takes ijn player and computer scores from main and prints them
def display_scores(p_scores, c_scores):
    print("Player: "+ str(p_scores))
    print("Computer: "+ str(c_scores))
    return
    
def main():
    print("Welcome to Rock-Paper-Scissors!")
    #Sets up the initial game state, as well as makes a while loop condition that can be changed later
    playing = True
    p_score = 0
    c_score = 0
    while playing:
        print("1. Play game")
        print("2: Show score")
        print("3: Quit")
        play = str(input())

        if play == "1":
           while True:
                #Start of game loop. If user selects "B", they exit to main menu
                #Otherwise, save user and computer weapon choices, determine winner, and update scores
                #No update to scores on a tie. THis loop continues until user selects "B"
                user_weapon = weapon_menu()
                if user_weapon == 0:
                    break
                else:
                    computer_weapon = comp_weapon()
                    winner = find_winner(user_weapon, computer_weapon)
                    if winner == 1: 
                        p_score += 1 
                    if winner == 2:
                        c_score += 1 
        elif play == "2":
            display_scores(p_score, c_score)
        elif play == "3":
            #First while loop break condition
            playing = False
        else:
            print("Invalid choice. Please try again.")

main()
