"""Script of game gcd."""
from brain_game.engine import run_game
from brain_game.games.progression import rules, get_question_and_answer


def main():
    """Do the game and returns on screen the result of game of user."""
    run_game(rules, get_question_and_answer)


if __name__ == '__main__':
    main()
