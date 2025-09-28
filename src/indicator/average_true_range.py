from typing import List, Optional


def average_true_range(opens: List[float], highs: List[float], lows: List[float], closes: List[float], period: int) -> List[Optional[float]]:
    return_value: List[Optional[float]]
    length: int
    true_range: List[float]
    sum_true_range: float
    atr_prev: float

    if period <= 0:

        raise ValueError("Period msut be greater than \"0\"!")
    
    length = len(highs)

    if length != len(lows) or length != len(closes):

        raise ValueError("Same length required for \"highs\", \"lows\", \"closes\"!")
    
    return_value = [None] * length  

    if length <= period:

        return return_value
    
    true_range = [0.0] * length

    for index in range(length):
        index: int
        prev_close: float
        r1: float
        r2: float
        r3: float

        prev_close = closes[index - 1] if index > 0 else closes[0]
        r1 = highs[index] - lows[index]
        r2 = abs(highs[index] - prev_close)
        r3 = abs(lows[index] - prev_close)
        true_range[index] = max(r1, r2, r3)

    sum_true_range = sum(true_range[:period])
    atr_prev = sum_true_range / period
    return_value[period - 1] = atr_prev

    for index in range(period, length):
        index: int

        atr_prev = (atr_prev * (period - 1) + true_range[index]) / period
        return_value[index] = atr_prev


    return return_value
