from datetime import date


class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome:str = nome
        self.nascimento:date = date.fromisoformat(nascimento)

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}"
        # return f"Olá, meu nome é {self.nome} e eu tenho {self.calcular_idade()} anos."

#     def calcular_idade(self):
#         hoje = date.today()
#         mes_nascimento = self.nascimento.month
#         dia_nascimento = self.nascimento.day
#         idade = hoje.year - self.nascimento.year
        
#         if hoje.month < mes_nascimento:
#         # if hoje.month < mes_nascimento or (hoje.month == mes_nascimento and hoje.day < dia_nascimento):
#             idade -= 1
        
#         return idade
    
    
class CalculadoraDeIdade:
    def calcular(self, pessoa:Pessoa):
        hoje = date.today()
        mes_nascimento = pessoa.nascimento.month
        dia_nascimento = pessoa.nascimento.day
        idade = hoje.year - pessoa.nascimento.year
        
        # if hoje.month < mes_nascimento:
        if hoje.month < mes_nascimento or (hoje.month == mes_nascimento and hoje.day < dia_nascimento):
            idade -= 1
        
        return idade
    
def calcular_idade(pessoa:Pessoa):
        hoje = date.today()
        mes_nascimento = pessoa.nascimento.month
        dia_nascimento = pessoa.nascimento.day
        idade = hoje.year - pessoa.nascimento.year
        
        # if hoje.month < mes_nascimento:
        if hoje.month < mes_nascimento or (hoje.month == mes_nascimento and hoje.day < dia_nascimento):
            idade -= 1
        
        return idade

    
if __name__ == "__main__":
    pessoa = Pessoa("Pedro", "2007-09-20")
    calculadora_de_idade = CalculadoraDeIdade()
    print(pessoa.apresentar())
    # print(pessoa.calcular_idade())
    print(calculadora_de_idade.calcular(pessoa))
    print(calcular_idade(pessoa))