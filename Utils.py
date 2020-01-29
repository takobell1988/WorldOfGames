import os


def scores_file_name():
    with open('Scores.txt', 'r') as scores:
        scoresdata = scores.read()
        print(scoresdata)
        return scoresdata


def bad_return_code():
    print('dont know yet')


def screen_cleaner():
    os.system('cls')

