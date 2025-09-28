from typing import List, Optional
from enum import Enum


class MovingAverageType(Enum):
    SIMPLE = "simple"
    WEIGHTED = "weighted"
    EXPONENTIONAL = "exponentional"


def moving_average(values: List[float], period: int, ma_type: MovingAverageType) -> List[Optional[float]]:
    return_value: List[Optional[float]]
    length: int

    if period <= 0:

        raise ValueError("Period must be greater than \"0\"!")

    length = len(values)
    return_value = [None] * length

    if length == 0:

        return return_value
    

    if MovingAverageType.SIMPLE == ma_type:
        total: float = 0.0

        for index, value in enumerate(values):
            index: int
            value: float

            total += value

            if index >= period:
                total -= values[index - period]


            if index >= period - 1:
                return_value[index] = total / period
    
    elif MovingAverageType.WEIGHTED == ma_type:
        weights: List[int]
        weighted_sum: float
        index: int

        weights = list(range(1, period + 1))
        weighted_sum = sum(weights)

        for index in range(period - 1, length):
            window: list[float]

            window = values[index - period + 1 : index + 1]
            return_value[index] = sum(weight * value for weight, value in zip(weights, window)) / weighted_sum

    elif MovingAverageType.EXPONENTIONAL == ma_type:
        ema: Optional[float]
        alpha: float

        alpha = 2 / (period + 1)
        ema = None

        for index, value in enumerate(values):
            index: int
            value: float

            if index < period - 1:

                continue


            if ema is None:
                ema = sum(values[index - period + 1 : index + 1]) / period

            else:
                ema = alpha * value + (1 - alpha) * ema
            
            return_value[index] = ema
            

    else:

        raise ValueError(f"Unsupported MovingAverageType: {ma_type}")


    return return_value