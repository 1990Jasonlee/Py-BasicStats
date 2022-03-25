import math
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

def zvariance(list: List[float]) -> float:
    for x in list:
        deviations = [(x - zmean(list)) ** 2]
        variance = sum(deviations) / zcount(list)

def zstddev(list: List[float]) -> float:
    return math.sqrt(zvariance(list))

def zstderr(list: List[float]) -> float:
    return zstddev(list) / math.sqrt(zcount(list))

def zcorr(listx: List[float], listy: List[float]) -> float:
    return cov(listx, listy) / zstddev(listx) * zstddev(listy)

def cov(listx: List[float], listy: List[float]) -> float:
    sum = 0
    if zcount(listx) == zcount(listy):
        for i in range(0, zcount(listx)):
            sum += ((listx[i] - zmean(listx)) * (listy[i] - zmean(listy)))
        return sum / (zcount(listx)-1)