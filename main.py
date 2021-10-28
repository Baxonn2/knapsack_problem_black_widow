from bwo import minimize

def funcion(x):
    return sum(x) ** 2

if __name__ == "__main__":
    print("Resultado: ", minimize(funcion, dof=5, maxiter=10000))