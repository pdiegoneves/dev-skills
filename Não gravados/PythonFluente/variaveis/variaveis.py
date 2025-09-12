# Variáveis são rótulos e não caixas

a = [1, 2, 3]

b = a

b.append(4)

print("a", a)
print("b", b)


# Variáveis são vinculados a objetos somente após serem criados

class Classe():
    def __init__(self):
        print(f"Classe   id: {id(self)}")
        
x = Classe()
y = Classe()

pessoa1 = {"Nome": "Joao Silva", "Nascimento" : 2000}

pessoa2 = pessoa1

print(pessoa2 is pessoa1)

print(id(pessoa1))
print(id(pessoa2))

pessoa2["Peso"] = 90

print("Pessoa1", pessoa1)

print("Igualdade", pessoa1 == pessoa2)

pessoa3 = {"Nome": "Joao Silva", "Nascimento" : 2000}

print(pessoa3 is pessoa1)

print(id(pessoa1))
print(id(pessoa3))

pessoa3["Altura"] = 177

print("Pessoa1", pessoa1)
print("Pessoa3", pessoa3)


t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 is t2)
print(t1 == t2)

print(id(t1))
print(id(t2))


l1 = [1, 2, 3]
l2 = list(l1)

print("IS", l1 is l2)
print("EQ", l1 == l2)

print(id(l1))
print(id(l2))

#As listas sã iguais, mas se referem a objetos diferentes

# Copia rasa
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print(l1)
print(l2)
print("ID tupla", id(l1[2]))

l2[1] += [33, 22] # objeto mutável lista alterado diretamente
l2[2] += (10, 11) # objeto imutável tupla cria ma nova e associa a variável

print("L1", l1)
print("L2", l2)
print("ID tupla", id(l2[2]))


print("=================")
import copy


class Sala:

    def __init__(self, alunos=None):
        self.alunos = alunos or []
        
    def __str__(self):
        return f"ALUNOS {self.alunos}"



sala1 = Sala(['Joao', 'Pedro', 'Paulo', 'Jose'])
sala2 = copy.copy(sala1)
sala3 = copy.deepcopy(sala1)

sala1.alunos.append("Maria")


print("sala1", id(sala1), sala1)
print("sala2", id(sala2), sala2)
print("sala3", id(sala3), sala3)

print("ID Alunos Sala1", id(sala1.alunos))
print("ID Alunos Sala2", id(sala2.alunos))
print("ID Alunos Sala3", id(sala3.alunos))


# print("IDS Salas", id(sala1), id(sala2), id(sala3))
# sala1.alunos.append('Felipe')
# print(sala2.alunos)
# print("IDS Alunos", id(sala1.alunos), id(sala2.alunos), id(sala3.alunos))
# sala3.alunos
