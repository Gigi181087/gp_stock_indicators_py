from typing import List, Optional


def _mfm_series(highs: List[float], lows: List[float], closes: List[float]) -> List[float]:
    return_value: List[float]
    length: int

    length = len(highs)

    if not (length == len(lows) == len(closes)):

        raise ValueError("Same length required for \"highs\", \"lows\" and \"closes\"!")
    
    return_value = [0.0] * length

    for index in range(length):
        index: int
        high: float
        low: float
        close: float
        denom: float

        high, low, close = highs[index], lows[index], closes[index]
        denom = high - low

        if denom == 0.0:
            return_value[index] = 0.0

        else:
            return_value[index] = ((close - low) - (high - close)) / denom


    return return_value


def chaikin_money_flow(highs: List[float], lows: List[float], closes: List[float], volumes: List[float], period: int) -> List[Optional[float]]:
    return_value: List[Optional[float]]
    length: int

    if period <= 0:

        raise ValueError("\"period\" must be greater than \"0\"!")
    
    length = len(highs)

    if not (length == len(lows) == len(closes) == len(volumes)):

        raise ValueError("Same length required for \"highs\", \"lows\", \"closes\" and \"volumes\"!")
    
    return_value = [None] * length

    if length < period:

        return return_value
    
    mfm_value = _mfm_series(highs, lows, closes)
    mfv_value = [mfm_value[index] * volumes[index] for index in range(length)]
    sum_mfv = sum(mfv_value[:period])
    sum_vol = sum(volumes[:period])
    return_value[period - 1] = (sum_mfv / sum_vol) if sum_vol != 0 else 0.0

    for index in range(period, length):
        sum_mfv += mfv_value[index] - mfv_value[index - period]
        sum_vol += volumes[index] - volumes[index - period]
        return_value[index] = (sum_mfv / sum_vol) if sum_vol != 0 else 0.0


    return return_value