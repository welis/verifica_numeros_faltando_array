"""
This script sorts a list of numbers and finds the missing numbers between them.
"""
numeros = [10,13,27,33,48]
numeros.sort()

for i in range(len(numeros)-1):
    if numeros[i+1] - numeros[i] > 1:
        missing = list(range(numeros[i]+1, numeros[i+1]))
        print(f"Entre {numeros[i]} e {numeros[i+1]} falta {missing}")

