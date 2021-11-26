from math import e
from random import random
from typing import List

def s1(x: float) -> float:
    return 1 / (1 + e**(-2*x))

def s2(x: float) -> float:
    return 1 / (1 + e**(-x))

def s3(x: float) -> float:
    return 1 / (1 + e**(-x/2))

def s4(x: float) -> float:
    return 1 / (1 + e**(-x/3))

def binarize(s_function, x_list: List[float]) -> List[int]:
    result = []
    
    for value in x_list:
        rand = random()
        T_value = s_function(value)

        #result.append(round(T_value))
        #result.append(abs(1 - BT) if rand <= T_value else 0)
        result.append(1 if rand <= T_value else 0)
    return result
