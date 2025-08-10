import re


def get_theme(tema):
    if tema == "dark":
        return "#0F2B38"
    elif tema == "light":
        return "#F2FAED"
    else:
        return "#FFB338"


print("IF ELSE")
print(get_theme("dark"))
print(get_theme("light"))
print(get_theme("other"))

print("MATCH CASE")


def get_theme2(tema):
    match tema:
        case "dark":
            return "#0F2B38"
        case "light":
            return "#F2FAED"
        case _:
            return "#FFB338"


print(get_theme2("dark"))
print(get_theme2("light"))
print(get_theme2("other"))


print("MOVIMENTOS")


def mover(movimento):
    match movimento:
        case ["frente", passos]:
            print("^" * passos)
        case ["tras", passos]:
            print("v" * passos)
        case ["esquerda", passos]:
            print("<" * passos)
        case ["direita", passos]:
            print(">" * passos)
        case _:
            print("Movimento inválido")


mover(["frente", 5])
mover(["tras", 3])
mover(["esquerda", 10])
mover(["direita", 3])

print("DICIONARIO")


def avaliar_retorno(retorno):
    match retorno:
        case {"status": 200}:
            print("Sucesso")
        case {"status": 404}:
            print("Não encontrado")
        case {"status": 500}:
            print("Erro interno do servidor")
        case _:
            print("Retorno desconhecido")


avaliar_retorno({"status": 200})
avaliar_retorno({"status": 404})
avaliar_retorno({"status": 500})
avaliar_retorno({"status": 201})

print("TIPOS")


def converte_para_int(num):
    match num:
        case bool():
            return "Não converto bool"
        case int():
            return num
        case float():
            return int(num)
        case str():
            num_re = re.sub(r"\D", "", num)
            try:
                return int(num_re)
            except ValueError:
                return ord(num)
        case _:
            return f"Não sei como converter o tipo: {type(num)}"


print("Interiro:", converte_para_int(10))
print("Float", converte_para_int(10.5))
print("String inteiro", converte_para_int("10"))
print("String float", converte_para_int("10.5"))
print("String", converte_para_int("a"))
print("String com número:", converte_para_int("a2"))
print("Boolean", converte_para_int(True))

print(isinstance(True, int))
