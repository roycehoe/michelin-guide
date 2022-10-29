import random
from typing import Literal

GameChoiceKeys = Literal[1, 2, 3]
GameChoiceValues = Literal["scissors", "paper", "stone"]
GAME_CHOICE_MAP: dict[GameChoiceKeys, GameChoiceValues] = {
    1: "scissors",
    2: "paper",
    3: "stone",
}

GameResults = Literal["win", "lose", "draw"]


class InvalidPlayerInputError(Exception):
    pass


def _get_player_input() -> GameChoiceKeys:
    try:
        player_choice = input(
            """Scissors, paper, stone?
1. Scissors
2. Paper
3. Stone
    """
        )
        return int(player_choice)
    except ValueError as e:
        raise InvalidPlayerInputError(e)


def _get_game_result(
    player_choice: GameChoiceValues, computer_choice: GameChoiceValues
) -> GameResults:
    if player_choice == computer_choice:
        return "draw"
    if player_choice == "scissors" and computer_choice == "paper":
        return "win"
    if player_choice == "paper" and computer_choice == "stone":
        return "win"
    if player_choice == "stone" and computer_choice == "scissors":
        return "win"
    return "lose"


def play():
    player_choice = GAME_CHOICE_MAP.get(_get_player_input(), None)
    computer_choice = GAME_CHOICE_MAP.get(random.randint(1, 3), None)

    game_result = _get_game_result(player_choice, computer_choice)
    game_result_logs = (
        f"You picked {player_choice}. Your opponent picked {computer_choice}"
    )

    print(f"You {game_result}. {game_result_logs}")
    print("goodbye")
    exit()


play()
