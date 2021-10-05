#!/usr/bin/env python
"""Introduce of a person."""

import prompt


def welcome_user():
    """Ask user`s name. Returns it."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    return user_name
