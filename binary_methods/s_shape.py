from math import e

def s1(x: float) -> float:
    return 1 / (1 + e**(-2*x))

def s2(x: float) -> float:
    return 1 / (1 + e**(-x))

def s3(x: float) -> float:
    return 1 / (1 + e**(-x/2))

def s4(x: float) -> float:
    return 1 / (1 + e**(-x/3))