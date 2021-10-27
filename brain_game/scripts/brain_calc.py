"""Script of game calculator."""
from brain_game.engine import start
from brain_game.games.calc import rules, play


def main():
    """Do the game and returns on screen the result of game of user."""
    start(rules, play)


if __name__ == '__main__':
    main()
