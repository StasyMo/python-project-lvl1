"""Script of game if_even."""
from brain_game.engine import start
from brain_game.games.even import rules, task


def main():
    """Do the game and returns on screen the result of game of user."""
    start(rules, task)


if __name__ == '__main__':
    main()
