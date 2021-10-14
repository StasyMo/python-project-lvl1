from random import randint
from brain_game.scripts import brain_games
from brain_game.games.check_user_answer import check_answer
from brain_game.games.correct_answers import gcd_correct_answer


def gcd_game():
    user_name = brain_games.main()
    count_answers = 0
    ANSWERS_TO_WIN = 3
    print('Find the greatest common divisor of given numbers.')
    while count_answers < ANSWERS_TO_WIN:
        UP_RANGE = 100
        gcd_number1 = randint(1, UP_RANGE)
        gcd_number2 = randint(1, UP_RANGE)
        print('Question: {0} {1} '.format(gcd_number1, gcd_number2),
              'Your answer: ', end='')
        user_answer = input()
        try:
            user_answer = int(user_answer)
        except ValueError:
            return print("The answer might be a number, but '{0}' "
                         "is not a number ;(. \n Let's try again, "
                         "{1}!".format(user_answer, user_name))
        correct_answer = gcd_correct_answer(gcd_number1, gcd_number2)
        count_answers = check_answer(correct_answer, user_answer, count_answers,
                                     ANSWERS_TO_WIN, user_name)
        count_answers += 1
    if count_answers == ANSWERS_TO_WIN:
        # если игрок ошибкся, фукнция check_user_answer
        # вернёт максимальное значение, а в
        # последнем шаге while мы это значение увеличим
        print('Congratulations, {}!'.format(user_name))
