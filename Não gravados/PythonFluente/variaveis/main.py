def rotulos():
    """Variáveis são róulos e não caixas"""
    a = [1, 2, 3]
    b = a

    print("a == a", a == a)
    print("a is b", a is a)

    b.append(4)

    print("a", a)
    
def criacao_objetos():
    """Variáveis são vinculadas a objetos somente após serem criados"""
    class Classe():
        def __init__(self):
            print(f"Classe   id: {id(self)}")
            
    x = Classe()
    y = Classe()

def rotulos_dicionarios():
    """Os dicionários são iguais, mas se referem a objetos diferentes"""
    pessoa1 = {"Nome": "Joao Silva", "Nascimento" : 2000}
    pessoa2 = pessoa1
    pessoa3 = {"Nome": "Joao Silva", "Nascimento" : 2000}

    print("pessoa2 is pessoa1", pessoa2 is pessoa1)
    print("pessoa3 is pessoa1", pessoa3 is pessoa1)
    

    print("id(pessoa1)", id(pessoa1))
    print("id(pessoa2)", id(pessoa2))
    print("id(pessoa3)", id(pessoa3))


    print("pessoa1 == pessoa2", pessoa1 == pessoa2)
    print("pessoa1 == pessoa3", pessoa1 == pessoa3)

    pessoa2["Peso"] = 90
    pessoa3["Altura"] = 177

    print("Pessoa1", pessoa1)
    print("Pessoa2", pessoa2)
    print("Pessoa3", pessoa3)


def rotulos_mutaveis_imutaveis():
    """Copia e Referência"""
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
    print("l1 == l2", l1 == l2)
    
    print("l1 is l3", l1 is l3)
    print("l1 == l3", l1 == l3)
    
    print("l1 is l4", l1 is l4)
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

    print("id(l1[1])", id(l1[1]))
    print("id(l2[1])", id(l2[1]))
    print("id(l1[2])", id(l1[2]))
    print("id(l2[2])", id(l2[2]))

    l2[1] += [33, 22]
    l2[2] += (10, 11)

    print("l1", l1)
    print("l2", l2)

    print("id(l1[2])", id(l1[2]))
    print("id(l2[2])", id(l2[2]))


def copia_rasa_vs_copia_profunda():
    """"""
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

    sala2.alunos.remove("Pedro")
    sala3.alunos.append("Jonas")

    print("sala1", id(sala1), sala1)
    print("sala2", id(sala2), sala2)
    print("sala3", id(sala3), sala3)

    
def parametro_de_funcao():
    """A função pode alterar qualquer objeto mutável passado para ela"""
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

    time_da_escola = ["Atleta 1", "Atleta 2", "Atleta 3", "Atleta 4", "Atleta 5"]
    
    class Onibus:
        def __init__(self, passageiros=None):
            # self.passageiros = passageiros or []
            self.passageiros = list(passageiros) or []
        
        def embarcar(self, nome):
            self.passageiros.append(nome)

        def desembarcar(self, nome):
            self.passageiros.remove(nome)

    onibus = Onibus(time_da_escola)

    onibus.desembarcar("Atleta 3")

    print("Onibus", onibus.passageiros)
    print("Time da Escola", time_da_escola)

if __name__ ==  "__main__":
    # rotulos()
    # criacao_objetos()
    # rotulos_dicionarios()
    # rotulos_mutaveis_imutaveis()
    # copia_rasa()
    # copia_rasa_vs_copia_profunda()
    # parametro_de_funcao()
    perigo()