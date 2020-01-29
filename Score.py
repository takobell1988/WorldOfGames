from Live import load_game

gamevalues = load_game()
difficulty = gamevalues[1]


# def points_of_winning():
#     gamevalue = load_game()
#     difficulty = (gamevalue[1] * 3) + 5
#     print(difficulty)
#     return difficulty

#
# points_of_winning()

def add_score(difficulty):
    try:
        with open('Scores.txt', 'r') as scores:
            current_score = scores.read()
            print("score.txt points: " + str(current_score))
    except BaseException as e:
        print("cannot read scores.txt file, creating new one")
        open("Scores.txt", "w+")

    points_of_winning = (difficulty * 3) + 5
    print("win points: " + str(points_of_winning))
    new_score = int(current_score) + points_of_winning
    print("new score is : " + str(new_score))
    a = open('Scores.txt', 'w+')
    a.write(str(new_score))





add_score(difficulty)