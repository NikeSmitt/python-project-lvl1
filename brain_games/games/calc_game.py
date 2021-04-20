import random
import prompt
import brain_games.game_loop

GAME_MESSAGE = "What is the result of the expression?"
TOP = 30
BOTTOM = 1


def add_(a, b):
    return a + b, f"{a} + {b}"


def sub_(a, b):
    return a - b, f"{a} - {b}"


def mult_(a, b):
    return a * b, f"{a} * {b}"


def calc_game():
    a = random.randint(BOTTOM, TOP)
    b = random.randint(BOTTOM, a)
    operation = random.choice([add_, sub_, mult_])
    result, question = operation(a, b)
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ")
    return user_answer, str(result)


def main():
    brain_games.game_loop.main(GAME_MESSAGE, calc_game)


if __name__ == "__main__":
    main()