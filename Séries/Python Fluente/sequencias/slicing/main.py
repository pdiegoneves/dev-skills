import array

import numpy as np
import pandas as pd

print("--- Fatiamento com Strings ---")
minha_string = "Python é Incrível!"
print(f"String original: '{minha_string}'")
print(f"minha_string[0:6]: '{minha_string[0:6]}'") 
print(f"minha_string[:6]: '{minha_string[:6]}'")   
print(f"minha_string[3:-2]: '{minha_string[3:-2]}'")
print(f"minha_string[7:]: '{minha_string[7:]}'")  
print(f"minha_string[:]: '{minha_string[:]}'")  
print(f"minha_string[::2]: '{minha_string[::2]}'") 
print(f"minha_string[::-1]: '{minha_string[::-1]}'")
print("--- Fatiamento com Strings ---\n\n")


print("--- Fatiamento com Listas ---")
minha_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Lista original: {minha_lista}")

print(f"minha_lista[2:5]: {minha_lista[2:5]}")  
print(f"minha_lista[-3:]: {minha_lista[-3:]}")     
print(f"minha_lista[:-2]: {minha_lista[:-2]}")  
print(f"minha_lista[1:8:3]: {minha_lista[1:8:3]}") 
print("--- Fatiamento com Listas ---\n\n")


print("--- Fatiamento com Tuplas ---")
minha_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tupla original: {minha_tupla}")
print(f"minha_tupla[3:7]: {minha_tupla[3:7]}")
print(f"minha_tupla[::-1]: {minha_tupla[::-1]}")
print("--- Fatiamento com Tuplas ---")


print("--- Fatiamento com Arrays ---")
meu_array = array.array('i',[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Array original: {meu_array}")

print(f"meu_array[2:5]: {meu_array[2:5]}")  
print(f"meu_array[-3:]: {meu_array[-3:]}")     
print(f"meu_array[:-2]: {meu_array[:-2]}")  
print(f"meu_array[1:8:3]: {meu_array[1:8:3]}") 
print("--- Fatiamento com Arrays ---\n\n")


print("--- Fatiamento com Arrays NumPy ---")

meu_array_1d = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(f"Array 1D original: {meu_array_1d}")
print(f"meu_array_1d[3:7]: {meu_array_1d[3:7]}") 

meu_array_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print(f"\nArray 2D original:\n{meu_array_2d}")
print(f"meu_array_2d[0:2, :]:\n{meu_array_2d[0:2, :]}")
print(f"meu_array_2d[:, 1:3]:\n{meu_array_2d[:, 1:3]}")
print(f"meu_array_2d[1:3, 0:2]:\n{meu_array_2d[1:3, 0:2]}")
print(f"meu_array_2d[1:3:-1, 0:2]:\n{meu_array_2d[1:3:-1, 0:2]}")
print(f"meu_array_2d[1:3, 0:2:-1]:\n{meu_array_2d[1:3, 0:2:-1]}")
print("--- Fatiamento com Arrays NumPy ---\n\n")

print("--- Fatiamento com DataFrames Pandas ---")
data = {
    'Nome': ['Alice', 'Bob', 'Carlos', 'Diana', 'Eva'],
    'Idade': [24, 27, 22, 32, 29],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
}
meu_dataframe = pd.DataFrame(data)
print(f"DataFrame original:\n{meu_dataframe}")
print(f"\nmeu_dataframe[1:3]:\n{meu_dataframe[1:3]}")
print(f"\nmeu_dataframe.loc[1:3]:\n{meu_dataframe.loc[1:3]}")
print(f"\nmeu_dataframe.iloc[1:3]:\n{meu_dataframe.iloc[1:3]}")
print(f"\nmeu_dataframe.iloc[0:2, 0:2]:\n{meu_dataframe.iloc[0:2, 0:2]}")
print(f"\nmeu_dataframe['Idade']:\n{meu_dataframe['Idade']}")
print(f"\nmeu_dataframe[['Nome', 'Cidade']]:\n{meu_dataframe[['Nome', 'Cidade']]}")

# print(f"\nmeu_dataframe[0:2, 0:2]:\n{meu_dataframe[0:2, 0:2]}") --> Gera um erro de InvalidIndexError

print("--- Fatiamento com DataFrames Pandas ---\n\n")
