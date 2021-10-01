#!/usr/bin/env python
"""Main script of project brain_game."""
from brain_game.cli import welcome_user


def main():
    """Launch function to ask user`s name. Returns name of user."""
    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main()
