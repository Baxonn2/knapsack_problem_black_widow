from random import random, choice

def calculadora(alpha, v1, v2):
    return (alpha * v1) + ((12 - alpha)*v2) - 6

min_ = 10000
max_ = -10000

for i in range(100000):
    alpha = random() * 12
    v1 = 1
    v2 = 1
    
    result = calculadora(alpha, v1, v2)
    min_ = min(min_, result)
    max_ = max(max_, result)
    
print(f"{min_=}")
print(f"{max_=}")