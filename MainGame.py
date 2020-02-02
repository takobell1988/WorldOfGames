import time
import os
from Live import load_game, welcome
from Score import create_score_file
create_score_file()
input_name = input('Enter yor name here: ')
start_over = 0


while start_over != str("exit"):
    time.sleep(2)
    os.system('cls')
    welcome(input_name)
    time.sleep(2)
    load_game()
    start_over = input('\n' + '\n' + 'Press Enter to start over or "exit" to Exit: ')
