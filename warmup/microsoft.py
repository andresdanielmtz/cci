"""
Example

Uno me sorprendio de lo facil jaja supongo era para ver si usaba logica o me iba como cochi a la mier** a buscar combinaciones.... una arreglo de longitud par, con numeros enteros, decir si hay forma de colocar los numeros en parejas de tal forma que todas las sumas de parejas den impar
"""

def makePairs(arr: list[int]) -> bool:
    # If the array is odd, not even worth it.
    if len(arr) % 2 == 1: 
        return False
    
    odd = [num for num in arr if num % 2 == 1]
    even = [num for num in arr if num % 2 == 0]
    
    # if their length isn't the same, it isn't possible to pair all of them such that the sum of the pairs is impair. 
    return len(odd) == len(even)
    