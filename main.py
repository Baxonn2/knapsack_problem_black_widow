from typing import List
from bwo import minimize
from knapsack import KnapsackProblem, BadSolutionException
from binary_methods.q_shape import q1, q2, q3, q4
from datetime import datetime

files_path = [
    "instances/knapPI_1_1000_1000_1",
    "instances/knapPI_2_100_1000_1",
    "instances/knapPI_3_100_1000_1",
    "instances/knapPI_1_200_1000_1",
    "instances/knapPI_2_200_1000_1",
    "instances/knapPI_3_200_1000_1",
    "instances/knapPI_1_500_1000_1",
    "instances/knapPI_2_500_1000_1",
    "instances/knapPI_3_500_1000_1",
    "instances/knapPI_1_1000_1000_1",
    "instances/knapPI_2_1000_1000_1",
    "instances/knapPI_3_1000_1000_1",
    "instances/knapPI_1_2000_1000_1",
    "instances/knapPI_2_2000_1000_1",
    "instances/knapPI_3_2000_1000_1"
]

files_name = [
    "knapPI_1_100_1000_1",
    "knapPI_2_100_1000_1",
    "knapPI_3_100_1000_1",
    "knapPI_1_200_1000_1",
    "knapPI_2_200_1000_1",
    "knapPI_3_200_1000_1",
    "knapPI_1_500_1000_1",
    "knapPI_2_500_1000_1",
    "knapPI_3_500_1000_1",
    "knapPI_1_1000_1000_1",
    "knapPI_2_1000_1000_1",
    "knapPI_3_1000_1000_1",
    "knapPI_1_2000_1000_1",
    "knapPI_2_2000_1000_1",
    "knapPI_3_2000_1000_1"
]


def generate_problem(file_path: str) -> KnapsackProblem:
    values = []
    weights = []
    capacity = 0
    first_line = True
    with open(file_path, "r") as file:
        lines = file.read().split("\n")
        for index, line in enumerate(lines):
            line_list = line.strip().split(" ")
            if first_line:
                capacity = int(line_list[1])
                first_line = False
            elif index == len(lines)-2:
                #print(line_list)
                break
            else:
                v, w = line_list
                values.append(int(v))
                weights.append(int(w))
            
    return KnapsackProblem(values, weights, capacity)

problem = generate_problem(files_path[0])

def funcion(x):
    try:
        problem.set_solution(x)
    except BadSolutionException as error:
        return error.total_weight
    return - problem.get_total_value()

def print_status(file_path, q_function, iteracion):
    strtime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{strtime} - evaluando: {file_path} con funcion: {q_function}, iteracion {iteracion}/31", end=" ")

if __name__ == "__main__":
    
    for file_path, file_name in zip(files_path, files_name):
        for q_function in [q1, q2, q3, q4]:
            for iteration in range(31):
                print_status(file_name, q_function.__name__, iteration)
                problem = generate_problem(file_path)
                
                inverted_total_value, solution, history = minimize(
                    funcion, 
                    q_function,
                    dof=len(problem.items), 
                    #x0=[0.5] * len(values),
                    bounds=[(-3, 3)] * len(problem.items),
                    pp=0.95,
                    cr=0.05,
                    pm=0.8,
                    npop=20, 
                    maxiter=100,
                    disp=True
                )
                
                total_value = - inverted_total_value
                binary_solution = solution
                print(f"{total_value=}")
                #print(f"{solution=}")
                #print(f"{binary_solution=}")
                #problem.print_result()
                
                with open(f"resultados/{file_name} - {q_function.__name__}.csv", "a") as file:
                    file.write(f"{iteration}," + ",".join(history) + "\n")