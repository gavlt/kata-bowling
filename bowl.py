from typing import List, Optional, Tuple, Union

"""
Simple bowling:
 1. The score is the sum of all the frames, each frame consists of 1 or 2 throws
 2. If a frame consists of a single throw which knocks down all 10 pins, the next frame is doubled
 3. If a frame consists of 2 throws which knock down all 10 pins, 
 the next *throw* is doubled (i.e. the first throw in the next frame)
 4. You can assume you won't be handed anything invalid, i.e. no frames scoring 11, no games with too many frames, etc.
"""

def score(frames: List[Tuple[int,Optional[int]]]) -> int:
    total = 0
    is_strike = False
    is_spare = False
    for (first,second) in frames:
        total = apply_throws(total, first, second, is_strike, is_spare)
        is_strike = second is None
        is_spare = not is_strike and (first + second) == 10
    return total

def apply_throws(total, first_throw, second_throw, is_strike, is_spare) -> int:
    total += first_throw * (2 if is_strike or is_spare else 1)
    if second_throw:
        total += second_throw * (2 if is_strike else 1)
    return total