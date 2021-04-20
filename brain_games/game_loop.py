import prompt


GAME_ATTEMPTS = 3


def get_wrong_message(user_answer, right_answer):
    return f"'{user_answer}' is wrong answer ;(. Correct answer was " \
           f"'{right_answer}'."


def get_message(message, name):
    return f"{message}, {name}!"


def main(welcome_message=None, game=None):
    name = prompt.string("May I have your name? ").capitalize()
    print(f"Hello, {name}!")
    print(welcome_message)
    message = "Congratulations"
    for _ in range(GAME_ATTEMPTS):
        user_answer, right_answer = game()
        if user_answer == right_answer:
            print("Correct!")
        else:
            print(get_wrong_message(user_answer, right_answer))
            message = "Let's try again"
            break
    print(get_message(message, name))


if __name__ == "__main__":
    main()
