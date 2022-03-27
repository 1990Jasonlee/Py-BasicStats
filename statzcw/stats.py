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
    index = (list_length - 1) // 2
    if list_length % 2 == 0:
        return sorted_number[index]
    else:
        return sorted_number[index] + sorted_number[index + 1] / 2

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

def readDataSets(files):
    data = {}
    for file in files:
        data[file] = readDataSets(files)
        return data

def read_data_file(files):
    x , y = [], []
    with open(files) as file:
        newline = file.line()
        for line in file:
            row = line.split(',')
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x, y
