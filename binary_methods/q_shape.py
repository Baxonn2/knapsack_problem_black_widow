from math import sqrt
from typing import List
from random import random
import numpy as np

def q1(x: float, x_max = 6) -> float:
    if x < 0.5 * x_max:
        return abs(x / (0.5 * x_max))
    return 1

def q2(x: float, x_max = 6) -> float:
    if abs(x) < 0.5 * x_max:
        return (x / (0.5 * x_max))**2
    return 1

def q3(x: float, x_max = 6) -> float:
    if x < 0.5 * x_max:
        return (x / (0.5 * x_max))**3
    return 1

def q4(x: float, x_max = 6) -> float:
    x = abs(x)
    if x < 0.5 * x_max:
        return sqrt(x / (0.5 * x_max))
    return 1

def binarize_a_bit(q_function, x: float) -> int:
    rand = random()
    return 1 if rand <= q_function(x, x_max=6) else 0

vectorized_function = np.vectorize(binarize_a_bit)

def binarize(q_function, x_list: np.ndarray) -> np.ndarray:
    #result = []
    
    return vectorized_function(q_function, x_list)
    
    #for value in x_list:
    #    rand = random()
    #    T_value = q_function(value, x_max=6)
    #    BT = round(T_value)
    #    #result.append(round(T_value))
    #    #result.append(abs(1 - BT) if rand <= T_value else 0)
    #    result.append(1 if rand <= T_value else 0)
    #return result
