from brain_game.scripts import brain_games
import prompt


def start(rules, play):
    user_name = brain_games.main()
    print(rules)
    count_answers = 0
    ANSWERS_TO_WIN = 3
    while count_answers < ANSWERS_TO_WIN:
        question, correct_answer = play()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        count_answers = comparing_answers(correct_answer, user_answer,
                                          count_answers,
                                          ANSWERS_TO_WIN, user_name)
        count_answers += 1
    if count_answers == ANSWERS_TO_WIN:
        print('Congratulations, {}!'.format(user_name))


def comparing_answers(correct_answer: int, user_answer: int, count_answers: int,
                      ANSWERS_TO_WIN: int, user_name: str):
    """Do match between correct answer and user`s answer.
    Prints the result of answerring and returns
    count_answers if correct. And the maximum number if not"""
    if correct_answer == user_answer:
        print('Correct!')
        return count_answers
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'. "
          "\nLet's try again, "
          "{2}!".format(user_answer, correct_answer, user_name))
    return ANSWERS_TO_WIN