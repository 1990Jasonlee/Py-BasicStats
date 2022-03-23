from typing import List
from statzcw.zcount import zcount


def zmean(list: List[float]) -> float:
    return sum(list) / zcount(list)
