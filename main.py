from typing import List
from bwo import minimize
from knapsack import KnapsackProblem, BadSolutionException
#from binary_methods.simple_binary import binarize
from binary_methods.q_shape import binarize, q1, q2, q3, q4

values = []
weights = []
capacity = 0
first_line = True
#with open("f1_l-d_kp_10_269", "r") as file:
with open("knapPI_3_100_1000_1", "r") as file:
    lines = file.read().split("\n")
    for index, line in enumerate(lines):
        line_list = line.strip().split(" ")
        if first_line:
            capacity = int(line_list[1])
            first_line = False
        elif index == len(lines):
            print(line_list)
            break
        else:
            v, w = line_list
            values.append(int(v))
            weights.append(int(w))
        
problem = KnapsackProblem(values, weights, capacity)
problem.print_result()


def funcion(x):
    try:
        problem.set_solution(binarize(q2, x))
    except BadSolutionException as error:
        return error.total_weight
    return - problem.get_total_value()

if __name__ == "__main__":
    inverted_total_value, solution = minimize(
        funcion, 
        dof=len(values), 
        #x0=[2] * len(values),
        bounds=[(-6, 6)] * len(values),
        #pp=0.5,
        #cr=0.8,
        #pm=0.7,
        npop=20, 
        maxiter=1000,
        disp=True
    )
    total_value = - inverted_total_value
    binary_solution = binarize(q2, solution)
    print(f"{total_value=}")
    print(f"{binary_solution=}")
    print(f"{solution=}")
    problem.print_result()