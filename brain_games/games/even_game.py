import random
import prompt
import brain_games.game_loop

WELCOME_MESSAGE = "Answer \"yes\" if the number is even,"\
        " otherwise answer \"no\"."
TOP = 100
BOTTOM = 1


def is_even(value) -> str:
    return "yes" if value % 2 == 0 else "no"


def even_game():
    value = random.randint(BOTTOM, TOP)
    print(f"Question: {value}")
    user_answer = prompt.string("Your answer: ")
    right_answer = is_even(value)
    return user_answer, right_answer


def main():
    brain_games.game_loop.main(WELCOME_MESSAGE, even_game)


if __name__ == "__main__":
    main()

