a = set(['a', 'b', 'c'])
b = set(['d', 'e', 'f'])
c = set(['a', 'e', 'g'])
d = set(['a'])


# Operadores de conjuntos

print("Intersecção")

print(a.intersection(b))
print(a & b)
print(a & c)

print("União")

print(a.union(b))
print(a | b)

print("Diferença")

print(a.difference(b))
print("O que em em a que não tem em b", a - b)
print("O que em em b que não tem em a", b - a)
print(a - c)

# -= é possível

#Comparações entre conjuntos
print("Comparações entre conjuntos")

print(d in a)
print('a' in a)
print(d <= a)
print(a <= d)
print(a >= d)

#Métodos adicionais de conjuntos
print("#Métodos adicionais de conjuntos")

a.add("d")

print(a)

aa = a.copy()
print(aa)

a.remove("c") #retorna None
print(a)

print(a.pop()) #retorna o elemento removido
print(a)

a.discard("a") #retorna None
a.discard("a") 

a.remove("c")