from math import atan, e, erf, pi, sqrt, tanh
from random import random
from typing import List

def v1(x: float) -> float:
    return abs(erf(sqrt(pi)*x/2))

def v2(x: float) -> float:
    return abs(tanh(x))

def v3(x: float) -> float:
    return abs(x/sqrt(1 + x**2))

def v4(x: float) -> float:
    return abs( 2 / pi * atan(pi * x /2 ))

def binarize(v_function, x_list: List[float]) -> List[int]:
    result = []
    
    for value in x_list:
        rand = random()
        T_value = v_function(value)

        #result.append(round(T_value))
        #result.append(abs(1 - BT) if rand <= T_value else 0)
        result.append(1 if rand <= T_value else 0)
    return result
