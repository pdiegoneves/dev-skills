# list = ["primeiro", "segundo", "terceiro"]


# def funcao(a, b, c, *d):
#     print("Argumento 1:", a)
#     print("Argumento 2:", b)
#     print("Argumento 3:", c)
#     print("demais argumentos:", d)


# funcao(*list)


# def desenpacotamento(*args):
#     for index, valor in enumerate(args):
#         print(f"Argumento {index + 1}: {valor}")


# lista = ["primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto"]
# desenpacotamento(*lista)

# list2 = {
#     "primeiro": "Pera",
#     "segundo": "Laranja",
#     "terceiro": "Banana",
#     "quarto": "Maça",
#     "quinto": "Uva",
# }


# def funcao2(primeiro=None, segundo=None, terceiro=None):
# def funcao2(primeiro=None, segundo=None, terceiro=None, **kwargs):
#     print(primeiro, segundo, terceiro, kwargs)


# funcao2(**list2)

# # outros usos

# a, b, c = range(3)
# print(a, b, c)

# a, b, c, *rest = range(50)
# print(a, b, c, rest)


# --------
# lista = [
#     "colher",
#     "garfo",
#     "faca",
#     "concha",
#     "espátula",
#     "abridor",
# ]

# colheres, garfos, facas, *demais_utensilios = lista

# print("Colheres:", colheres)
# print("Garfos:", garfos)
# print("Facas:", facas)
# print("Demais utensílios:", demais_utensilios)


def montar_macarronada(massa, molho, **ingredientes):
    print("Massa:", massa)
    print("Molho:", molho)
    print(ingredientes)


pedido = {
    "massa": "espaguete",
    "molho": "bolonhesa",
    "ingredientes": ["queijo", "azeitona", "cebola"],
}

montar_macarronada(**pedido)
