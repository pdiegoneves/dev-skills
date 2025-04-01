list = ["primeiro", "segundo", "terceiro"]


def funcao(a, b, c):
    print(a, b, c)


funcao(*list)


list2 = {
    "primeiro": "Pera",
    "segundo": "Laranja",
    "terceiro": "Banana",
    "quarto": "Maça",
}


# def funcao2(primeiro=None, segundo=None, terceiro=None):
def funcao2(primeiro=None, segundo=None, terceiro=None, **kwargs):
    print(primeiro, segundo, terceiro)


funcao2(**list2)

# outros usos

a, b, c = range(3)
print(a, b, c)

a, b, c, *rest = range(50)
print(a, b, c, rest)
