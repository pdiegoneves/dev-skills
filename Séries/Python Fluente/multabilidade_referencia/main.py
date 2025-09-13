
def rotulos():
    """Variáveis são róulos e não caixas"""

    a = [1, 2, 3]
    b = a 

    print("a == b", a == b)
    print("a is b", a is b)

    b.append(4)

    print("a", a)


def criacao_objeto():
    """Variáveis são vinculadas a objetos somente após serem criados"""

    class Classe:
        def __init__(self):
            print(f"Classe id: {id(self)}")

    x = Classe()
    y = Classe()

def rotulos_dicionario():
    """Os dicionários são iguais, mas se referem a objetos diferentes"""

    pessoa1 = {"Nome": "Joao Silva", "Nascimento" : 2000}
    pessoa2 = pessoa1
    pessoa3 = {"Nome": "Joao Silva", "Nascimento" : 2000}

    print("pessoa1 is pessoa2", pessoa1 is pessoa2)
    print("pessoa1 is pessoa3", pessoa1 is pessoa3)

    print("id(pessoa1)", id(pessoa1))
    print("id(pessoa2)", id(pessoa2))
    print("id(pessoa3)", id(pessoa3))

    print("pessoa1 == pessoa2", pessoa1 == pessoa2)
    print("pessoa1 == pessoa3", pessoa1 == pessoa3)

    pessoa2["Peso"] = 90
    pessoa3["Altura"] = 177

    print("pessoa1", pessoa1)
    print("pessoa2", pessoa2)
    print("pessoa3", pessoa3)

    print("pessoa1 == pessoa2", pessoa1 == pessoa2)
    print("pessoa1 == pessoa3", pessoa1 == pessoa3)


def rotulos_mutaveis_imutaveis():
    """Copia e referência"""
    t1 = (1, 2, 3)
    t2 = (1, 2, 3)

    print("t1 is t2", t1 is t2)
    print("t1 == t2", t1 == t2)

    print("id(t1)", id(t1))
    print("id(t2)", id(t2))

    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    l3 = l1
    l4 = list(l1)

    print("l1 is l2", l1 is l2)
    print("l1 is l3", l1 is l3)
    print("l1 is l4", l1 is l4)

    print("l1 == l2", l1 == l2)
    print("l1 == l3", l1 == l3)
    print("l1 == l4", l1 == l4)

    print("id(l1)", id(l1))
    print("id(l2)", id(l2))
    print("id(l3)", id(l3))
    print("id(l4)", id(l4))
    
def copia_rasa():
    """
        A princípio as cópias são rasas
        Os objetos internos são copiados por referência
    """

    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)

    print("l1 is l2", l1 is l2) 
    print("l1 == l2", l1 == l2)

    l1.append(100)
    l1[1].remove(55)

    print("l1", l1)
    print("l2", l2)

    print("id(l1)", id(l1))
    print("id(l2)", id(l2))
    print("id(l1[1])", id(l1[1]))
    print("id(l2[1])", id(l2[1]))
    print("id(l1[2])", id(l1[2]))
    print("id(l2[2])", id(l2[2]))

    l2[1] += [33, 22]
    l2[2] += (10, 11) # l2[2] = l2[2] + (10, 11)

    print("l1", l1)
    print("l2", l2)

    print("id(l1[2])", id(l1[2]))
    print("id(l2[2])", id(l2[2]))


def copia_rasa_vs_copia_profunda():
    import copy

    class Sala:
        def __init__(self, alunos=None):
            self.alunos = alunos or []

        def __str__(self):
            return f"Alunos: {self.alunos}"

    sala1 = Sala(['Joao', 'Pedro', 'Paulo', 'Jose'])
    sala2 = copy.copy(sala1) # Copia Rasa
    sala3 = copy.deepcopy(sala1) # Copia Profunda

    sala1.alunos.append('Maria')

    print("sala1", id(sala1), sala1)
    print("sala2", id(sala2), sala2)
    print("sala3", id(sala3), sala3)

    print("id(sala1.alunos)", id(sala1.alunos))
    print("id(sala2.alunos)", id(sala2.alunos))
    print("id(sala3.alunos)", id(sala3.alunos))

    sala2.alunos.remove("Pedro")
    sala3.alunos.append("Jonas")

    print("sala1", id(sala1), sala1)
    print("sala2", id(sala2), sala2)
    print("sala3", id(sala3), sala3)
    

def parametro_funcao():
    """A função pode alterar qualquer objeto mutável passado para ela como parametro"""

    def f(a, b):
        a += b
        return a
    
    x = 1 
    y = 2

    print("** x = 1, y = 2 **")
    print(f(x, y))
    print("x", x)
    print("y", y)

    x = [1, 2]
    y = [3, 4]

    print("** x = [1, 2], y = [3, 4] **")
    print(f(x, y))
    print("x", x)
    print("y", y)

    x = (1, 2)
    y = (3, 4)

    print("** x = (1, 2), y = (3, 4) **")
    print(f(x, y))
    print("x", x)
    print("y", y)



def perigo():
    """Perigo"""

    import copy

    # time_de_escola = [["Atleta 1", "Atleta 2", "Atleta 3", "Atleta 4", "Atleta 5"]]
    time_de_escola = ["Atleta 1", "Atleta 2", "Atleta 3", "Atleta 4", "Atleta 5"]

    class Onibus:
        def __init__(self, passageiros=None):
            # self.passageiros = copy.deepcopy(passageiros) or []
            # self.passageiros = passageiros[:] or []
            self.passageiros = list(passageiros) or []

        def embarcar(self, nome):
            # self.passageiros[0].append(nome)
            self.passageiros.append(nome)

        def desembarcar(self, nome):
            # self.passageiros[0].remove(nome)
            self.passageiros.remove(nome)

    onibus = Onibus(time_de_escola)

    onibus.embarcar("Aluno aleatório")

    onibus.desembarcar("Atleta 2")

    print("Passageiros:", onibus.passageiros)
    print("Time de escola:", time_de_escola)



if __name__ == '__main__':
    # rotulos()
    # criacao_objeto()
    # rotulos_dicionario()
    # rotulos_mutaveis_imutaveis()
    # copia_rasa()
    # copia_rasa_vs_copia_profunda()
    # parametro_funcao()
    perigo()