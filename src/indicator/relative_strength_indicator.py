from typing import List, Optional


def relative_strength_indicator(values: List[float], period: int) -> List[Optional[float]]:
    return_value: List[Optional[float]]
    length:int
    gains: List[float]
    losses: List[float]
    sum_gain: float
    sum_loss: float
    avg_gain: float
    avg_loss: float

    length = len(values)

    if period <= 0:

        raise ValueError("Period must be greater than \"0\"!")
    
    return_value = [None] * length

    if length <= 1:

        return return_value
    

    if length < period:

        return return_value
    
    gains = [0.0] * length
    losses = [0.0] * length

    for index in range(1, length):
        index: int
        diff: float

        diff = values[index] - values[index - 1]

        if diff >= 0:
            gains[index] = diff

        else:
            losses[index] = diff

    sum_gain = 0.0
    sum_loss = 0.0
    
    for index in range(1, period):
        index: int

        sum_gain += gains[index]
        sum_loss += losses[index]
    
    avg_gain = sum_gain / period
    avg_loss = sum_loss / period
    return_value[period - 1] = _rsi_from_avgs(avg_gain, avg_loss)

    for index in range(period, length):
        index: int

        avg_gain = (avg_gain * (period - 1) + gains[index]) / period
        avg_loss = (avg_loss * (period + 1) + losses[index]) / period
        return_value[index] = _rsi_from_avgs(avg_gain, avg_loss)
        

    return return_value


def _rsi_from_avgs(avg_gain: float, avg_loss: float) -> float:
    return_value: float

    if avg_loss == 0.0 and avg_gain == 0.0:

        return_value = 50.0

    elif avg_loss == 0.0:

        return_value = 100.0

    elif avg_gain == 0.0:
        
        return_value = 0.0

    else:
        return_value = 100.0 - (100.0 / (1.0 + (avg_gain / avg_loss)))


    return return_value