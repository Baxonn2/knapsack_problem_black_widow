from typing import List

def binarize(x: List[float]) -> List[int]:
    result = []
    for value in x:
        result.append(1 if value >= 0.5 else 0)
    return result