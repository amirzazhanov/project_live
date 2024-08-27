import random
import time
from Utils import screen_cleaner

class MemoryGame:
    def __init__(self, level):
        self.level = level

    # generate_sequence - Will generate a list of random numbers between 1 to 101. The list 
    # length will be difficulty.
    def generate_sequence(self):
        list = []
        for i in range(self.level):
            list.append(random.randint(1, 100))
        print(f"Generated list: {list}")
        time.sleep(2)
        screen_cleaner()
        return list

    # get_list_from_user - Will return a list of numbers prompted from the user. The list length 
    # will be in the size of difficulty.
    def get_list_from_user(self):
        list = []
        for i in range(self.level):
            list.append(int(input("Number 1-100: ")))
        return list

    # is_list_equal - A function to compare two lists if they are equal. The function will return 
    # True / False
    def is_list_equal(self, generated, user):
        return generated == user

    # play - Will call the functions above and play the game. Will return True / False if the user 
    # lost or won
    def play(self):
        return self.is_list_equal(self.generate_sequence(), self.get_list_from_user())
