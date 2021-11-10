from typing import List
from bwo import minimize
from knapsack import KnapsackProblem, BadSolutionException

values = [7,3,4,5,10]
weights = [1,2,3,1,2]
capacity = 3
problem = KnapsackProblem(values, weights, capacity)

def binarize(x: List[float]):
    result = []
    for value in x:
        result.append(1 if value >= 0.5 else 0)
    return result

def funcion(x):
    try:
        problem.set_solution(binarize(x))
    except BadSolutionException:
        return 0
    return - problem.get_total_value()

if __name__ == "__main__":
    inverted_total_value, solution = minimize(funcion, dof=len(values), npop=20, maxiter=100, disp=True)
    total_value = - inverted_total_value
    binary_solution = binarize(solution)
    print(f"{total_value=}")
    print(f"{binary_solution=}")