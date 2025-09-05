#Chose word or random?
#Print rules then gameboard
#check if guess right, wrong or alredy used
#chech if win or lose
#play again?
wrong_guess = 0

#print game board based on wrong_guess count
def game_doard(x):
    
    row1 = "\n    _____"
    row2 = "\n    |"  
    row3 = "\n    |"
    row4 = "\n    |"
    row5 = "\n    |"
    row6 = "\n    |"
    row7 = "\n  ---------"
    wrong2 = "\n    |   |" 
    wrong3 = "\n    |   O"
    wrong4 = "\n    |   |"
    wrong5 = "\n    |  /|"
    wrong6 = "\n    |  /|\\"
    wrong7 = "\n    |  /"
    wrong8 = "\n    |  / \\"
    match x:
        case 7:
            print(row1, row2, row3, row4, row5, row6, row7)
        case 6: 
            print(row1, wrong2, row3, row4, row5, row6, row7)
        case 5:
            print(row1, wrong2, wrong3, row4, row5, row6, row7)
        case 4:
            print(row1, wrong2, wrong3, wrong4, row5, row6, row7)
        case 3:
            print(row1, wrong2, wrong3, wrong5, row6, row7)            
        case 2:
            print(row1, wrong2, wrong3, wrong6, row7)
        case 1:
            print(row1, wrong2, wrong3, wrong6, wrong7)
        case 0:
            print(row1, wrong2, wrong3, wrong6, wrong8)     

#Takes word from user input
word = input("Chose a word. ").upper()

#Generate underscore for every char in word
wrong_letter = ""
line_display = ['_' for _ in word]
lives = 7

#loops until no lives left or word is correct
while lives > 0 and "_" in line_display:
    game_doard(lives)
    print( "\n" + ' '.join(line_display) + "\n Wrong letters: " + wrong_letter)
    guess = input("Chose a letter: ").upper()
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                if line_display[index] == "_":
                    line_display[index] = guess
                else: 
                    print("You have alredy guessed this letter. ")
    else:
        wrong_letter += guess
        print("Sorry wrong!")
        lives -= 1   
#print message if you guessed the word
if not "_" in line_display:
    print( "\n" + ' '.join(line_display))
    print("Congratulations")
#prints message if you lose
else:
    game_doard(lives)
    print("\n" + ' '.join(line_display) + "\n Wrong letters: " + wrong_letter)
    print("\n Sorry, you are out of guesses, the word was: " + word )    
                      