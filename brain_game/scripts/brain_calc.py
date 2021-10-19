"""Script of game calculator."""
from brain_game.games.engine_of_game import start_the_game, if_win_the_game
from brain_game.games.calc_module import calc_game


def main():
    """Do the game and returns on screen the result of game of user."""
    user_name, count_answers, ANSWERS_TO_WIN = start_the_game()
    count_of_answers = calc_game(user_name, count_answers, ANSWERS_TO_WIN)
    if_win_the_game(count_of_answers, ANSWERS_TO_WIN, user_name)


if __name__ == '__main__':
    main()
