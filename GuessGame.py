import random

class GuessGame:
    def __init__(self, level):
        self.level = level

    # generate_number - Will generate number between 1 to difficulty and save it to 
    # secret_number.

    def generate_number(self):
        return random.randint(1, self.level)

    # get_guess_from_user - Will prompt the user for a number between 1 to difficulty and 
    # return the number.
    def get_guess_from_user(self):
        return int(input(f"Enter number 1-{self.level}: "))

    # compare_results - Will compare the the secret generated number to the one prompted 
    # by the get_guess_from_user. 

    def compare_results(self, generated, user):
        return generated == user

    # play - Will call the functions above and play the game. Will return True / False if the user 
    # lost or won.

    def play(self):
        return self.compare_results(self.generate_number(),self.get_guess_from_user())