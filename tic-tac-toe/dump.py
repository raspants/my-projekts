"""
1. present roules and game operations
2. player choses symbol and if there is anoter player
3. generate board - klar
4. funktion if only one player
5. keep track of positions
6. determen if: win, lose ore draw
7. play again?
"""
import sys
import random

position_dict = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}
position_list = ("TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR")
player1, player2 = "X", "O"
global num_players
game_status = True
turn_coutn = 0

#funtion for quiting the game with exstra verification
def quit():
    x = input("\n Are you sure you want to quit? Y or N? ").upper()
    if x == "Y":
        print("\n Okey, good bye!")
        sys.exit()
        
    else:
        return x
    
#player character selection with exeption handeling
def player_setup():
    while True:
        x = input("\n Player1. \n Do u want to be X or O?  ").upper()
        if x == "X":
            y = "O" 
            print("\n Okey, player1 has chosen " + x + ". That means player2 will play as " + y + ". ")
            return x, y 
        elif x == "O":
            y = "X"
            print("\n Okey, player1 has chosen " + x +". That means player2 will play as " + y + ". ")
            return x, y
        else:
            print( "\n (" + x + ") is not a playable charakter")
            continue

#gör smartare - om ogämt tal genererat, kolla spelplan och gör ett smartare val
#generate move at random an validates, returns 1 if move is valide, else 0
def comp_move_gen(x):
    while True: 
        i = random.randint(0, 8)
        if position_dict[i] == " ":
            position_dict[i] = x
            print("\n Computer made it's move. ")
            print_board()
            return 1
        else:
            return 0

#validates move from player
def move_validation(x, y):
    if x == "Q":
        quit(x)
    else:
        if x in position_list:
            i = position_list.index(x)
            if position_dict[i] == " ":
                position_dict [i] = y
                return 1
            else:
                print("Invalid move, space alredy taken. ")
                return 0
        else:
            print("Invalid move, (" + x + ") position dose not exist. " )
            return 0  
        
#prints ta curent gameboard based on positions dictionary
def print_board():
    print("\n")
    print("\n")
    print("\n " + position_dict[0] + " | " + position_dict[1] + " | " + position_dict[2] + " ")
    print("------------")
    print(" " + position_dict[3] + " | " + position_dict[4] + " | " + position_dict[5] + " ")
    print("------------")
    print(" " + position_dict[6] + " | " + position_dict[7] + " | " + position_dict[8] + " ")


while game_status == True:
        
    choice = input("\n Hello and welkome to a game of Tic-Tac-Toe!/n First things first, i am not case sensitive so uper or lower case dose not mater. " 
                    "\n Do you know the rules of this game? Y for yes and N for no, and remember u can always quit by typing Q. ").upper()
    if choice == "Y":
        print("\n Great, then we skip introductions and get started right away. ")
    elif choice == "Q":
        quit()
    else:
        print("\n Thats fine. The goal is to get three in a row before youre oponent, simpel right! ")   

    num_players = input("\n Now you just nead to make two choices. First, are you 1 or 2 players? ")
    if num_players == 2:
        print("\n Great, lets go to the nexst step. ")
    else:
        print("Thats okay, then i will try to beat you! Now lets go to the nexst step!")
        
    player1, player2 = player_setup()


    print("\n The last thing we nead to check in is the gameboard and how we use it. Below you can se the gameboard and the 'comands' for the different positions. \n " \
    "For exampel on the top left you see TL and on the botom right you see BR, so all you nead to do is typ in the space u want on the gameboard when it's youre turn. \n Now.... LETS PLAY!!!")

    #gameboard exampel for players
    print(" " + "TL" + " | " + "TM" + " | " + "TR" + " ")
    print("--------------")
    print(" " + "ML" + " | " + "MM" + " | " + "MR" + " ")
    print("--------------")
    print(" " + "BL" + " | " + "BM" + " | " + "BR" + " ")
    break


while True:
    if turn_coutn < 9:        
        if num_players == 2:

            if turn_coutn % 2 == 0:
                curent_move = input(" \nPlayer1, make youre move.     ").upper()
                i = move_validation(curent_move, player1)
                turn_coutn += i    
            else:
                curent_move = input(" \nPlayer2, make youre move.     ").upper()
                i = move_validation(curent_move, player2)
                turn_coutn += i    
        else:
            if turn_coutn % 2 == 0:
                curent_move = input(" \nPlayer1, make youre move.     ").upper()
                i = move_validation(curent_move, player1)
                turn_coutn += i
            else:
                #calls to generate random move
                i = comp_move_gen(player2)
                turn_coutn += i
    else:
        print_board()
        new_game = input("\n Do you want to play again? Y, N?").upper
        match new_game:
            case "Y":
                turn_coutn = 0
            case "N":
                quit()            