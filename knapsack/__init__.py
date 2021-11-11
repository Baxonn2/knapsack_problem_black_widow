from typing import Any, List

class Item:
    
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight
        
class BadSolutionException(Exception):
    
    def __init__(self, total_weight, *args: object) -> None:
        super().__init__(*args)
        self.total_weight = total_weight
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)

class KnapsackProblem:
    
    items: List[Item]
    solution: List[bool]
    w_capacity: int
    
    def __init__(self, values: List[int], weights: List[int], 
                 w_capacity: int) -> None:
        assert len(values) == len(weights)
        
        # Inicializando items
        self.items = []
        self.solution = [False * len(values)]
        self.w_capacity = w_capacity
        
        for i in range(len(values)):
            new_item = Item(values[i], weights[i])
            self.items.append(new_item)
            
    def print_result(self):
        total_weights = 0
        total_value = 0
        count_selected = 0
        
        for index, selected in enumerate(self.solution):
            if selected:
                total_weights += self.items[index].weight
                total_value += self.items[index].value
                count_selected += 1
        
        print("Resumen:")
        print(f"Capacidad de la mochila = {self.w_capacity}")
        print(f"Capacidad utilizada = {total_weights}")
        print(f"Cantidad de items guardados = {count_selected}")
        print(f"Cantidad total de items = {len(self.items)}")
        print(f"Valor total guardado: {total_value}")
        
    def set_solution(self, solution: List[bool]):
        if self.is_valid_solution(solution):
            self.solution = solution
        else:
            total_weight = 0
            for index, selected in enumerate(solution):
                if selected:
                    total_weight += self.items[index].weight
            raise BadSolutionException(total_weight)
        
    def get_total_value(self):
        total_value = 0
        for index, selected in enumerate(self.solution):
            if selected:
                total_value += self.items[index].value
        return total_value
    
    def is_valid_solution(self, solution: List[bool]) -> bool:
        """
        Comprueba si la solucion es válida o no

        Parameters
        ----------
        solution : List[bool]
            Solucion que se quiere comprobar si es valida

        Returns
        -------
        bool
            Retorn True si es valida t False en caso contrario
        """
        total_weights = 0
        
        if len(solution) > len(self.items):
            return False
        
        for index, selected in enumerate(solution):
            if selected:
                total_weights += self.items[index].weight
                if total_weights > self.w_capacity:
                    return False
        
        return True
        
        

if __name__ == '__main__':
    values = [2,3,4,5,10]
    weights = [1,2,3,1,2]
    #n_items = len(values)
    capacity = 2
    #picks = knapsack_dp(values,weights,n_items,capacity)
    #print(picks)
    problem = KnapsackProblem(values, weights, capacity)
    problem.set_solution([0, 0, 0, 0, 1])
    problem.print_result()