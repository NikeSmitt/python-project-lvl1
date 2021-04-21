import random
import brain_games.game_loop


GAME_MESSAGE = "What number is missing in the progression?"
STEP_BOTTOM = 2
STEP_TOP = 10
SEQ_BOTTOM = 2
SEQ_TOP = 50
SEQ_COUNT = 10


def progression_game():
    step = random.randint(STEP_BOTTOM, STEP_TOP)
    start_seq = random.randint(SEQ_BOTTOM, SEQ_TOP)
    seq = [str(x) for x in range(start_seq, start_seq + SEQ_COUNT * step, step)]
    remove_idx = round(random.random() * SEQ_COUNT)
    right_answer = seq[remove_idx]
    seq[remove_idx] = '..'
    return " ".join(seq), right_answer


def main():
    brain_games.game_loop.main(GAME_MESSAGE, progression_game)


if __name__ == "__main__":
    main()
