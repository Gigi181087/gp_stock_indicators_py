from typing import List, Optional, Tuple


def swing_points(highs: List[float], lows: List[float], left: int, right: int) -> Tuple[List[Optional[float]], List[Optional[float]]]:
    return_swing_highs: List[Optional[float]]
    return_swing_lows: List[Optional[float]]
    length: int

    if left <= 0 or right <= 0:

        raise ValueError("left/right must be greater than \"0\"!")
    

    if len(highs) != len(lows):

        raise ValueError("Same length required for \"highs\", \"lows\"!")
    
    length = len(highs)
    return_swing_highs = [None] * length
    return_swing_lows = [None] * length

    if 0 == length:

        return return_swing_highs, return_swing_lows
    
    left_offset = left
    right_offset = right

    for index_i in range(left_offset, length - right_offset):
        index_i: int
        high_0: float
        low_0: float
        is_swing_high: bool
        is_swing_low: bool

        high_0 = highs[index_i]
        low_0 = lows[index_i]
        is_swing_high = True
        is_swing_low = True

        for index_j in range(index_i - left_offset, index_i + right_offset + 1):
            index_j: int

            if index_i == index_j:

                continue


            if highs[index_j] > high_0:
                is_swing_high = False


            if lows[index_j] < low_0:
                is_swing_low = False


            if not is_swing_high and not is_swing_low:

                break
        

        if is_swing_high:
            return_swing_highs[index_i] = high_0


        if is_swing_low:
            return_swing_lows[index_i] = low_0


    return return_swing_highs, return_swing_lows