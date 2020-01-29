from currency_converter import CurrencyConverter
import random
import time
time.sleep(0.7)

c = CurrencyConverter()


def get_money_interval(difficulty):
    rate = c.convert(1, 'USD', 'ILS')
    # print('curancy rate ' + str(rate))
    # print('dificulty is ' + str(choice[1]))
    generate_usd = random.randint(1, 100)
    global t
    t = int(generate_usd) * rate
    # print('the total nis amount ' + str(t))
    interval_points = (t - (5 - difficulty)), (t + (5 - difficulty))
    # print('the interval points are ' + str(interval_points))

    print("How much are " + str(generate_usd) + "$ (USD) in NIS today ? ")
    return interval_points


def get_guess_from_user():
    user_guess = input('Make a guess...  : ')
    return int(user_guess)


def play_currency_game(difficulty):
    print("****** Welcome to Currency Roulette Game! ******" + "\n")
    interval_range = get_money_interval(difficulty)
    guess = get_guess_from_user()
    print('Your guess is ' + str(guess))
    if guess < int(interval_range[0]) or guess > int(interval_range[1]):
        time.sleep(1)
        print('You are Wrong!')
        time.sleep(1)
        print('The EXACT value is ' + str("%.2f" % t) + ' NIS')
    else:
        time.sleep(1)
        print('Your Right! :0')
        time.sleep(1)
        print('The EXACT value is ' + str("%.2f" % t) + ' NIS')


