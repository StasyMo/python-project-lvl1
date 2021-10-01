"""Take users answer and returns the result: if it is correct or not."""


def check_answer(correct_answer: int, user_answer: int, count_answers: int,
                 answers_to_win: int, user_name: str):
    """Do match between correct answer and user`s answer.
    Prints the result of answerring and returns
    count_answers if correct. And the maximum number if not"""
    if correct_answer == user_answer:
        print('Correct!')
        return count_answers
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'. "
          "\n Let's try again, "
          "{2}!".format(user_answer, correct_answer, user_name))
    return answers_to_win
