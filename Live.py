import time
from MemoryGame import play_memory_game
from GuessGame import play_guess_game
from CurrencyRouletteGame import *


def welcome(input_name):
    print("\n" + "Hello " + input_name + " and welcome to the World Of Games (WoG)." +
          "\n" + "Here you can find many cool games to play." + "\n")


def load_game():
    print('\n' + "Please choose a game to play:" + '\n' +
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back" + "\n" +
          "2. Guess Game - guess a number and see if you chose like the computer. " + '\n' +
          "3. Currency Roulette - try and guess the value of random amount of USD in ILS." + "\n")

    chosen_game = int(input("Enter the number of the game here: "))

    while chosen_game > 3 or chosen_game < 1:
        print("Invalid game number")
        chosen_game = int(input("Choose game number between 1 to 3: "))

    difficulty = int(input("Choose game difficulty between 1 to 5: "))

    while difficulty > 5 or difficulty < 1:
        print("invalid difficulty")
        difficulty = int(input("Choose game difficulty between 1 to 5: "))
    try:
        if chosen_game == 1:
            play_memory_game(difficulty)
            return chosen_game, difficulty
        elif chosen_game == 2:
            play_guess_game(difficulty)
            return chosen_game, difficulty
        elif chosen_game == 3:
            play_currency_game(difficulty)
            return chosen_game, difficulty

    except BaseException as e:
        print('Error: Game not found')
        print(e.args)
