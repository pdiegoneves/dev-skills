from paciente import Paciente
def imprimir_objetos(paciente1: Paciente, paciente2: Paciente) -> None:
    print(paciente1)
    print(f"Igualdade: {paciente1 == paciente2}")




def main():
    paciente1 = Paciente("Joao Silva", "01/01/2000")
    paciente2 = Paciente("Joao Silva", "01/01/2000")

    imprimir_objetos(paciente1, paciente2)

    # paciente1.nome = "Maria Silva"
    # print(paciente1)
    print("Hash", hash(paciente1))

    print(paciente1.calcular_idade())
    print(paciente1.maior_de_idade())
    


if __name__ == '__main__':
    main()

