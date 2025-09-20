# Funções em python são objetos de primeira classe
"""
Criada durante a execução de um programa

Atribuída a uma variável ou a um elemento em uma estrutura de dados

Passada como argumento para uma função

Devolvida como o resultado de uma função
"""

def ola_mundo():
    return "Olá Mundo!"

print(type(ola_mundo))

print(ola_mundo())


# Funções de ordem superior
# Uma função que recebe uma função como argumento ou devolve uma função como resultado é uma função de ordem superior

def dobro(n):
    return n * 2

lista = list(map(dobro, [1, 2, 3, 4, 5]))

print(lista)

# Funções anônimas

fruits = ["Banana", "maça", "manga"]

print(sorted(fruits, key=lambda x: len(x)))


# É possível fazer uma classe ser invocável
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __call__(self, *args, **kwds):
        print(f"Eu sou {self.nome} e tenho {self.idade} anos")
    
    
p = Pessoa("Diego", 39)

p()

# Paramentros apenas posicionais

def soma(a, b):
    return a + b

print(soma(1, 2))
# print(soma(a=1, 2))
print(soma(a=1, b=2))
print(soma(1, b=2))

def multi(a, b, /):
    return a * b

print(multi(2, 3))
# print(multi(a=1, b=2))