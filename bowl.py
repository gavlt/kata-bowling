from annotated_types import Ge
from typing import List, Optional, Tuple, Callable, Annotated
from functools import partial
from dataclasses import dataclass

"""
Simple bowling:
 1. The score is the sum of all the frames, each frame consists of 1 or 2 throws
 2. If a frame consists of a single throw which knocks down all 10 pins, the next frame is doubled
 3. If a frame consists of 2 throws which knock down all 10 pins, 
 the next *throw* is doubled (i.e. the first throw in the next frame)
 4. You can assume you won't be handed anything invalid, i.e. no frames scoring 11, no games with too many frames, etc.
"""

PositiveInt = Annotated[int, Ge(0)]
FrameType = Tuple[PositiveInt, Optional[PositiveInt]]
GameType = List[FrameType]


def apply_throws(total, first_throw, second_throw, is_strike, is_spare) -> int:
    total += first_throw * (2 if is_strike or is_spare else 1)
    if second_throw:
        total += second_throw * (2 if is_strike else 1)
    return total


def score(frames: GameType, *, apply_throws_fn: Callable = apply_throws) -> int:
    if len(frames) > 10:
        raise ValueError("Cannot have more than 10 frames!")
    total = 0
    is_strike = False
    is_spare = False
    for (first, second) in frames:
        if first < 0 or (second is not None and second < 0):
            raise ValueError("Scores cannot be negative!")
        if first + (second or 0) > 10:
            raise ValueError("A frame cannot score over 10!")
        total = apply_throws_fn(total, first, second, is_strike, is_spare)
        is_strike = second is None
        is_spare = not is_strike and (first + second) == 10
    return total


"""
House Rules Bowling:
 A house rules spec initially contains a count for the total pins and a strike multiplier
 1. Implement `house_rules` so that it returns the correct score function for a given total_pins and strike_multiplier
 2. Decide on your own house rule and add it to the scoring function
"""


@dataclass
class HouseRulesSpec:
    darts_goal: int


def house_rules_darts(spec: HouseRulesSpec) -> Callable[[GameType], int]:
    def apply_darts_throws(*args) -> int:
        total = apply_throws(*args)
        if total > spec.darts_goal:
            total = (
                spec.darts_goal
                if total % spec.darts_goal == 0
                else total % spec.darts_goal
            )
        return total

    return partial(score, apply_throws_fn=apply_darts_throws)


def house_rules(spec: HouseRulesSpec) -> Callable[[GameType], int]:
    def my_score(g: GameType) -> int:
        total = score(g)
        if total > spec.darts_goal:
            total = (
                spec.darts_goal
                if total % spec.darts_goal == 0
                else total % spec.darts_goal
            )
        return total

    return my_score
