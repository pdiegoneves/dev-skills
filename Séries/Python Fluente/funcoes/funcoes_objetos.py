# Funções em python são objetos de primeira classe
"""
Criada durante a execução de um programa
Atribuída a uma variável ou a um elemento em uma estrutura de dados
Passada como argumento para uma função
Devolvida como o resultado de uma função
"""

def ola_mundo():
    return "Óla mundo"

print(ola_mundo())
print(type(ola_mundo()))
print(ola_mundo)
print(type(ola_mundo))

print("Funções de Ordem Superior")

def dobro(n):
    return n * 2

print(dobro(2))

lista_numeros = [1, 2, 3, 4, 5]

lista_dobro = list(map(dobro, lista_numeros))

print(lista_dobro)

print("Classe como função")

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __call__(self):
        print(f"Meu nome é {self.nome}")
    

p = Pessoa("João")

p()

print("Paramentros apenas posicionais")

def soma(a, b):
    return a + b

print(soma(1, 2))
print(soma(2, b=2))
print(soma(b=3, a=2))
# print(soma(b=1, 2))# Gera erro

def mult(a, b, /):
    return a * b

print(mult(5, 2))