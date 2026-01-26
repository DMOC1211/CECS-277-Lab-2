
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

    #For simplicity, 1 = Rock, 2 = Paper, 3 = Scissors
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
    
def comp_weapon():
    return random.randint(1, 3)

def find_winner(p_wep, c_wep): 
    ## tie = 0,  player_win = 1, computer_win = 2
    if p_wep = c_wep:
        return 0
    if p_wep = 1 and c_wep = 3:
        return 1
    if p_wep = rock and c_wep = paper:
        return 2
    if p_wep = scissors and c_wep = rock:
        return 2
    if p_wep = scissors and c_wep = paper:
        return 1
    if p_wep = paper and c_wep = rock:
        return 1
    if p_wep = paper and c_wep = scissors:
        return 2



def display_scores(p_scores, c_scores):
    print("Player: "+ p_scores)
    print('Computer: " + c_scores)
    return



score = 0 
    if find_winner == 1 
        score += 1
    if find_winner == 2 
        score -= 1
    if find_winner == 0 
        return
    
def main():
    print("Welcome to Rock-Paper-Scissors!")
    playing = True
    while playing:
        print("1. Play game")
        print("2: Show score")
        print("3: Quit")
        play = int(input())
        if play == 1:
           while True:
            user_weapon = weapon_menu()
            if user_weapon != 0:
                computer_weapon = random.randint(1, 3)
                
            else:
                break
        elif play == 2:
            print("te", "st")
        elif play == 3:
            playing = False
        else:
            print("Invalid choice. Please try again.")

main()
