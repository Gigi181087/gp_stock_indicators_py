from typing import List, Optional

def on_balance_volume(closes: List[float], volumes: List[float]) -> List[Optional[float]]:
    return_value: List[Optional[float]]
    on_balance_volume_value: float

    if len(closes) != len(volumes):

        raise ValueError("Same length required for \"closes\" and \"volumes\"!")
    
    length = len(closes)
    return_value = [None] * length

    if length <= 1:

        return return_value
    
    on_balance_volume_value = 0.0

    for index in range(1, length):
        index: int

        if closes[index] > closes[index - 1]:
            on_balance_volume_value += volumes[index]

        elif closes[index] < closes[index - 1]:
            on_balance_volume_value -= volumes[index]

        return_value[index] = on_balance_volume_value


    return return_value
