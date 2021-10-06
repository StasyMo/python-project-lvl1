"""Script of game gcd."""

from random import randint
from brain_game.scripts import brain_games
from brain_game.games.check_user_answer import check_answer
from brain_game.games.correct_answers import progression_correct_answer


def main():
    """Do the game and returns on screen the result of game of user."""
    user_name = brain_games.main()
    count_answers = 0
    answers_to_win = 3
    PROGRESSION_LENGTH = 10
    UP_RANGE = 10
    print('What number is missing in the progression?')
    while count_answers < answers_to_win:
        progression = [0] * PROGRESSION_LENGTH
        progression[0] = randint(0, UP_RANGE)
        progression_step = randint(1, UP_RANGE)
        missed_elem = randint(0, UP_RANGE - 1)
        i = 1
        print('Question: ', end='')
        correct_answer = progression_correct_answer(progression,
                                                    progression_step,
                                                    missed_elem, i,
                                                    PROGRESSION_LENGTH)
        print('Your answer: ', end='')
        user_answer = input()
        try:
            user_answer = int(user_answer)
        except ValueError:
            return print("The answer might be a number, but '{0}' "
                         "is not a number ;(. \n Let's try again, "
                         "{1}!".format(user_answer, user_name))
        count_answers = check_answer(correct_answer, user_answer, count_answers,
                                     answers_to_win, user_name)
        count_answers += 1
    if count_answers == answers_to_win:
        # если игрок ошибкся, фукнция check_user_answer
        # вернёт максимальное значение, а в
        # последнем шаге while мы это значение увеличим
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()
