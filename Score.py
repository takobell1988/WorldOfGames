def create_score_file():
    file = open('Scores.txt', 'w')
    file.write("0")
    file.close()


def add_score(difficulty):
    try:
        file = open('Scores.txt', 'r')
        current_score = file.read()
        print("old score points: " + str(current_score))
        points_of_winning = (difficulty * 3) + 5
        print("win points: " + str(points_of_winning))
        new_score = int(current_score) + int(points_of_winning)
        print("new score is : " + str(new_score))
        file = open('Scores.txt', 'w')
        file.write(str(new_score))
        file.close()

    except BaseException as e:
        print("ERROR : cannot read scores.txt file")





