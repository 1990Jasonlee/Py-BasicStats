from typing import List


def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)
