from paciente import Paciente

def calcular_idade(dada_nascimento):
    ano_nascimento = int(dada_nascimento.split('/')[2])
    ano_atual = 2025
    return ano_atual - ano_nascimento

def maior_de_idade(paciente):
    idade = calcular_idade(paciente.data_nascimento)
    return idade >= 18


def main():
    paciente1 = Paciente("Joao da Silva", "01/01/2000")
    paciente2 = Paciente("Joao da Silva", "01/01/2000")

    print(paciente1)
    print(paciente2)
    print(f"Igualdade: {paciente1 == paciente2}" )

    print(hash(paciente1))
    
    # paciente1.nome = "Jose"
    print(paciente1)
    
    print(f"Idade: {calcular_idade(paciente1.data_nascimento)}")
    print(f"Maior de idade: {maior_de_idade(paciente1)}")
    

if __name__ == '__main__':
    main()

