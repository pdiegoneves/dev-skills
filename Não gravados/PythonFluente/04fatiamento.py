list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[0:3])
print(list[:3])
print(list[3:])
print(list[::-1])

print(list[3:6])
print(list[3:6:2])

# Por que fatias excluem o último item?
"""
- É fácil ver o tamanho da fatia ou da faixa quando apenas a posição final é dada: 
    tanto range(3) quanto my_list[:3] produzem três itens.

- É fácil calcular o tamanho de uma fatia ou de uma faixa quando o início e o fim são dados: basta subtrair fim-início.

- É fácil cortar uma sequência em duas partes em qualquer índice x, sem sobreposição: simplesmente escreva 
"""
