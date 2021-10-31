"""Script of game if_even."""
from brain_game.engine import run_game
from brain_game.games.even import rules, get_question_and_answer


def main():
    """Do the game and returns on screen the result of game of user."""
    run_game(rules, get_question_and_answer)


if __name__ == '__main__':
    main()
