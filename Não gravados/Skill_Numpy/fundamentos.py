import numpy as np

from timed import get_time


@get_time
def lista_lenta():
    lista_lenta = list(range(1_000_000))
    lista_dobrada = [i * 2 for i in lista_lenta]


@get_time
def array_rapido():
    array_rapido = np.arange(1_000_000)
    array_dobrado = array_rapido * 2


lista_lenta()
array_rapido()


meu_primeiro_array = np.array([1, 2, 3, 4, 5])
print(meu_primeiro_array)
print(type(meu_primeiro_array))
print(meu_primeiro_array.dtype)
print(meu_primeiro_array.shape)
print("Dobrar", meu_primeiro_array * 2)
print("Soma", meu_primeiro_array + 2)

"""
A maioria dos arrays NumPy tem algumas restrições. Por exemplo:
    1. Todos os elementos da matriz devem ser do mesmo tipo de dados.
    2. Uma vez criado, o tamanho total do array não pode ser alterado.
    3. O formato deve ser “retangular”, não “irregular”; 
    por exemplo, cada linha de uma matriz bidimensional deve ter o mesmo número de colunas.
"""

print("======= Parte 2 =======")
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:3]

print(a)
print(b)

b[-1] = 99

print(a)
print(b)

c = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
print(c)

print("Atributos")
print("Shape", c.shape)
print("Ndim", c.ndim)
print("Size", c.size)
print("Type", c.dtype)


d = np.array([1.2, 3.14, 5.4])
print(d)
print(d.dtype)


print("======= Parte 3 =======")
print("np.zeros() , np.ones(), np.empty(), np.arange(),np.linspace()")
# Criar array com 0s
a = np.zeros(5)
print(a)

# Criar array com 1s
b = np.ones(5)
print(b)

# Criar array vazio
c = np.empty(5)
print(c)

# Criar array com range
d = np.arange(5)
print(d)
e = np.arange(2, 9, 2)  # Primeiro elemento, último elemento, tamanho do passo
print(e)

# Criar array com linspace - linearmente espaçado
f = np.linspace(0, 10, num=5)  # Primeiro elemento, último elemento, número de elementos
print(f)

# Especificar o dtype
g = np.ones(2, dtype=np.int64)
print(g)
print(g.dtype)


print("======= Parte 4 =======")
print("np.sort() ,np.concatenate()")

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(arr)
print(np.sort(arr))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a)
print(b)

c = np.concatenate((a, b))
print(c)
print(a + b)  # Não concatena

print("======= Parte 5 =======")
print("arr.reshape()")
# Não pode mudar o total de elementos

a = np.arange(6)
print(a)

b = a.reshape(3, 2)
print(b)

print("======= Parte 6 =======")
print("np.newaxis ,np.expand_dims")
print("np.newaxis")
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
print(a)
row_vector = a[np.newaxis, :]
print(row_vector.shape)
print(row_vector)
col_vector = a[:, np.newaxis]
print(col_vector.shape)
print(col_vector)

print("np.expand_dims")

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
print(a)
b = np.expand_dims(a, axis=1)
print(b.shape)
print(b)
c = np.expand_dims(a, axis=0)
print(c.shape)
print(c)

print("======= Parte 7 =======")
print("Selecionar valores")

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
five_up = a >= 5
print(a[five_up])
print("Pares", a[a % 2 == 0])
print("Duas condições", a[(a % 2 != 0) & (a < 9)])
print("Duas condições", a[(a % 2 != 0) | (a > 9)])

five_up = (a > 5) | (a == 5)
print(five_up)

b = np.nonzero(a < 5)
print(b)

lista_de_coordenadas = list(zip(b[0], b[1]))
for coord in lista_de_coordenadas:
    print(coord)

print(a[b])

print("======= Parte 8 =======")
print("slicing and indexingnp.vstack()np.hstack()np.hsplit().view()copy()")

# https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-create-an-array-from-existing-data

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr1 = a[3:8]
print(arr1)

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))

x = np.arange(1, 25).reshape(2, 12)
print(x)

print(np.hsplit(x, 3))
print(np.hsplit(x, (3, 4)))


b1 = a1.copy()

print(b1)
b1[0] = 999
print(b1)
print(a1)

print("======= Parte 9 =======")
print("Operações de matriz")

arr1 = np.array([1, 2])
arr2 = np.ones(2, dtype=int)
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print(arr1.sum())

arr3 = np.array([[1, 1], [2, 2]])
print(arr3.sum(axis=0))
print(arr3.sum(axis=1))

print("======= Parte 10 =======")
print("Operações com escalar")

data = np.array([1, 2])
print(data * 1.6)
print(data + 10)

print("======= Parte 11 =======")
print("Mais operações")

print(data.max())
print(data.min())
print(data.sum())

a = np.array(
    [
        [0.45053314, 0.17296777, 0.34376245, 0.5510652],
        [0.54627315, 0.05093587, 0.40067661, 0.55645993],
        [0.12697628, 0.82485143, 0.26590556, 0.56917101],
    ]
)

print(a.min(axis=0))  # minimo de cada coluna
print(a.min(axis=1))  # minimo de cada linha

rng = np.random.default_rng()

print(rng.integers(5, size=(2, 4)))

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
print(unique_values)
b = np.array(
    [
        1,
        1,
        1,
        1,
        2,
        3,
        3,
        3,
        3,
        3,
    ]
)
unique_values = np.unique(b)
print(unique_values)

unique_values, indices_list = np.unique(b, return_index=True)
print(indices_list)
unique_values, counters = np.unique(b, return_counts=True)
print(counters)

print("======= Parte 12 =======")
print("Transposição de Matrizes")

data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
print(data.reshape(2, 3))
print(data.T)

print("Inverter")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.flip(arr))
arr_2d = np.array([[1, 1, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6]])
print(np.flip(arr_2d))
print(np.flip(arr_2d, axis=0))
print(np.flip(arr_2d, axis=1))

print("======= Parte 12 =======")
print("Achatamento")
print(arr_2d.flatten())  # cria uma visão, se alterar altera o original
print(arr_2d.ravel())  # cria uma cópia

print("======= Parte 13 =======")
print("Salvando array")

np.save("teste", arr_2d)
np.savetxt("teste.csv", arr_2d)
b = np.load("teste.npy")
c = np.loadtxt("teste.csv")
print(b)
print(c)


import matplotlib.pyplot as plt

# %matplotlib inline
plt.plot(a)
plt.show()
