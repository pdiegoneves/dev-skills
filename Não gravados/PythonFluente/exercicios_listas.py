# Exercicio 1

numeros = [6,5,4,7,9,2,4,6,1]

numeros.sort()
print(numeros)

# Exercício 2

produtos = (
    {'nome': 'Celular', 'preco': 1500},
    {'nome': 'Fone de Ouvido', 'preco': 100},
    {'nome': 'Tablet', 'preco': 3500}
)

produtos_por_preco = sorted(produtos, key=lambda item: item['preco'])
print(produtos_por_preco)

# Exercício 3
produtos_por_letras = sorted(produtos, key=lambda x: len(x['nome']))
print(produtos_por_letras)
