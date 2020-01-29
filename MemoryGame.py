import time
import os
import random


def generate_sequence(difficulty):
    print("Try to remember the numbers! : ")
    random_list = random.sample(range(1, 101), difficulty)
    time.sleep(2)
    print(random_list)
    time.sleep(0.7)
    os.system('cls')
    # print("Try to remember the numbers!")
    time.sleep(3)
    return random_list


def get_list_from_user(difficulty):
    print("WHAT WAS THE NUMBERS?? (Write each num at the same order and press Enter) : ")
    user_list = []
    for i in range(0, difficulty):
        user_num = int(input('num: '))
        user_list.append(user_num)
    print("Your chosen numbers are : " + str(user_list))
    time.sleep(3)
    return user_list


def is_list_equal(a, b):
    if a == b:
        print("CORRECT answer! :) ")
        time.sleep(2)
        print("See you next time !")
        time.sleep(3)
        return True
    else:
        print("This is a WRONG answer !")
        time.sleep(2)
        print("See you next time ! :)")
        time.sleep(3)
        return False


def play_memory_game(user_input):
    print("****** Welcome to the Memory Game! ******" + "\n")
    a = generate_sequence(user_input)
    b = get_list_from_user(user_input)
    is_list_equal(a, b)









