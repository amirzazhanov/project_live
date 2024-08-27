import random

class CurrencyRouletteGame:
    def __init__(self, level):
        self.level = level
        self.ex_rate = 3.69 # --> 2024/08/27

# get_money_interval - Will get the current currency rate from USD to ILS and will 
# generate an interval as follows: 
#   a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))

    def get_money_interval(self, usd):
        return usd * self.ex_rate + self.level - 5 , usd * self.ex_rate + 5 - self.level

# get_guess_from_user - A method to prompt a guess from the user to enter a guess of 
# value to a given amount of USD
    def get_guess_from_user(self, usd):
        return float(input(f"Guess the value in ILS for {usd} USD: "))

# play - Will call the functions above and play the game. Will return True / False if the user 
# lost or won
    def play(self):
        usd = random.randint(1, 100)
        interval = self.get_money_interval(usd)
        user = self.get_guess_from_user(usd)
        return interval[0] <= user <= interval[1]