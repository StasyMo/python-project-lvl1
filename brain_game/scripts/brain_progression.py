"""Script of game gcd."""
from brain_game.games.engine_of_game import engine_of_game
from brain_game.games.progression_module import rules_of_the_game, \
    task_of_the_game


def main():
    """Do the game and returns on screen the result of game of user."""
    engine_of_game(rules_of_the_game, task_of_the_game)


if __name__ == '__main__':
    main()
