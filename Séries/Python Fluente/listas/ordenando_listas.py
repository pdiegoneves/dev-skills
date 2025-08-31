print("===== list.sort() =====")


lista = [ 5,2,4,1,3]
print(lista)
lista.sort()
print(lista)

lista2 = lista.sort()
print(lista2)


print("===== list.sort() =====")
print("===== sorted()=====")


lista3 = [ 5,2,4,1,3]
print(lista3)
nova_lista = sorted(lista3)
print(nova_lista)

tupla = ( 5,2,4,1,3)
print("TUPLA",tupla)
nova_lista2 = sorted(tupla)
print(nova_lista2)


print("===== sorted()=====")


#REVERSE

lista_desordenada1 = [5, 2, 9, 1, 5, 6]
lista_desordenada2 = [5, 2, 9, 1, 5, 6]

lista_desordenada1.sort(reverse=True)
print("Com sort:", lista_desordenada1)


lista_ordenada_reversa = sorted(lista_desordenada2, reverse=True)
print("Com sorted:", lista_ordenada_reversa)



# KEY
frutas1 = ['banana', 'maçã', 'laranja', 'uva', 'manga']
frutas2 = ['banana', 'maçã', 'laranja', 'uva', 'manga']

frutas1.sort()
print("Com sort sem key:", frutas1)
frutas1.sort(key=len)
print("Com sort com key:", frutas1)

print("Sorted com key:", sorted(frutas2, key=len))


# Key avança
lista_de_espera = [('Maria', 19), ('João', 22), ('Ana', 21), ('Pedro', 20), ('Carla', 23), ('José', 70)]

lista_ordenada_por_idade = sorted(lista_de_espera, key=lambda aluno: aluno[1], reverse=True)

print(lista_ordenada_por_idade)