from typing import List

def zcount(list: List[float]) -> float:
    return len(list)


def zmean(list: List[float]) -> float:
    return sum(list) / zcount(list)


def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)


def zmedian(list: List[float]) -> float:
    sorted_number = sorted(list)
    list_length = len(list)
    index = list_length / 2
    return sorted_number[index]

