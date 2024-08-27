
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

#
#  This function has a person name as an input and returns a string in the following layout:
#
def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
#
#  This function Gets an input from the user about the game he chose. After receiving the game number from 
#  the user, the function will get the level of difficulty with the following text and also save to a 
#  variable:
#
def load_game():
    print ("Please choose a game to play:\n")
    print ("\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print ("\t2. Guess Game - guess a number and see if you chose like the computer")
    print ("\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while True:
            game = int(input("Enter game number (1-3): "))
            if game >=1 and game <= 3:
                break
    
    while True:
            level = int(input("Please choose game difficulty level 1-5: "))
            if level >=1 and level <= 5:
                break
    match game:
        case 1:
            result = MemoryGame(level).play()
        case 2:
            result = GuessGame(level).play()
        case 3:
            result = CurrencyRouletteGame(level).play()
    print (f"game result\n")
    if result:
         print("+1")
         add_score(level)
    else:
         print("-1")
   
    return game, level