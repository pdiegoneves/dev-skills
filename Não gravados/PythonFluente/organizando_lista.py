lista_desordenada1 = [5, 2, 9, 1, 5, 6]
lista_desordenada2 = [5, 2, 9, 1, 5, 6]

# SORT

#lista_desordenada1.sort()

if lista_desordenada1.sort():
    print("Organizou")
else:
    print("Não organizou")

print(lista_desordenada1)
# retorna none

#SORTED

if sorted(lista_desordenada2):
    print("Organizou")
else:
    print("Não organizou")

print(lista_desordenada2)

lista_ordenada = sorted(lista_desordenada2)
print(lista_ordenada)   

# REVERSE
lista_reversa = sorted(lista_desordenada2, reverse=True)
print(lista_reversa)
lista_desordenada1.sort(reverse=True)
print(lista_desordenada1)

# key
frutas = ['banana', 'maçã', 'laranja', 'uva', 'manga']

print(sorted(frutas))
print(sorted(frutas, key=len))

lista_de_espera = [('Maria', 19), ('João', 22), ('Ana', 21), ('Pedro', 20), ('Carla', 23)]

print(sorted(lista_de_espera, key=lambda x: x[1], reverse=True))
