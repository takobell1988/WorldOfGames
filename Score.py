
def add_score(difficulty):
    try:
        with open('Scores.txt', 'r') as scores:
            current_score = scores.read()
            if current_score == None:
                a = open('Scores.txt', 'w+')
                a.write("0")
            print("old score points: " + str(current_score))
    except BaseException as e:
        print("cannot read scores.txt file, creating new one")
        # a = open('Scores.txt', 'w+')
        # a.write("0")
        current_score = 0

    points_of_winning = (difficulty * 3) + 5
    print("win points: " + str(points_of_winning))
    new_score = int(current_score) + int(points_of_winning)
    print("new score is : " + str(new_score))
    a = open('Scores.txt', 'w')
    a.write(str(new_score))




