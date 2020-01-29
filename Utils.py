import os
import time
import random


def scores_file_name():
    with open('Scores.txt', 'r') as scores:
        scoresdata = scores.read()
        print(scoresdata)
        return scoresdata


scores_file_name()