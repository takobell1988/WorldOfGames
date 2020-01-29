from Live import load_game


def points_of_winning():
    gamevalue = load_game()
    score = (gamevalue[1] * 3) + 5
    print(score)
    return score


points_of_winning()