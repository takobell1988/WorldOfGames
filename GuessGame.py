import random
import time


def generate_number(difficulty):
    global secret_number
    secret_number = random.randint(1, int(difficulty))


def get_guess_from_user(difficulty):
    global user_guess
    user_guess = input("please guess a number from 1 to " + str(difficulty) + ": ")
    return user_guess


def compare_results():
    if secret_number == int(user_guess):
        print("You are right!")
        time.sleep(1)
        print('See you next time! :)')
        return True
    else:
        print("You are Wrong!")
        time.sleep(1)
        print("The correct number is " + str(secret_number))
        time.sleep(1)
        print('See you next time! :)')
        return False


def play_guess_game(user_input):
    print("****** Welcome to the Guess Game! ******" + "\n")
    generate_number(user_input)
    get_guess_from_user(user_input)
    compare_results()





