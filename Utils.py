import os


def scores_file_name():
    file = open('Scores.txt', 'r')
    scoresdata = file.read()
    print(scoresdata)
    return scoresdata


def bad_return_code():
    print('dont know yet')


def screen_cleaner():
    os.system('cls')

