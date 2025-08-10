# Sequências Planas e Sequências de Container
pessoas = [("João", 38), ("Maria", 25)]


import array

meu_array = array.array("i", [1, 2, 3, 4])

### Type codes
# - `'i'`: inteiro (int)
# - `'f'`: float
# - `'d'`: double (float mais preciso)

meu_array.append(5)
meu_array.append(20)
meu_array.append(6)

meu_array.remove(20)

meu_array.insert(0, 99)
# meu_array.append(3.14) - Gera erro


print(type(meu_array))
print(meu_array)
print(meu_array)
print(meu_array[2])

print("+++++++++")
for i, num in enumerate(meu_array):
    print(i, num)

# Sequências Mútaveis, Sequências Imutáveis
print("Mutáveis")
print("Meu array inicial", meu_array)
meu_array[5] = 50
print("Meu array final", meu_array)

print("Imutáveis")
frase = "honestidade em pequenas coisas não é uma coisa pequena"

print(frase)
# frase[0] = "H"
print(frase)
frase = "Honestidade em pequenas coisas não é uma coisa pequena"
print(frase)


print(pessoas)
pessoas[0] = ("José", 34)
print(pessoas)
# pessoas[0][1] = 24
print(type(pessoas))
print(type(pessoas[0]))
print(pessoas)
