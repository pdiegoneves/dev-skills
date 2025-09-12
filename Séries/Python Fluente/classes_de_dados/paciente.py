# class Paciente():
#     def __init__(self, nome, data_nascimento):
#         self.nome = nome
#         self.data_nascimento = data_nascimento

#     def __str__(self):
#         return f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"

# from collections import namedtuple

# Paciente = namedtuple(
#     "Paciente",
#     ["nome", "data_nascimento"]
# )

# import typing

# Paciente = typing.NamedTuple(
#     "Paciente",
#     [
#         ("nome", str),
#         ("data_nascimento", str)
#     ]
# )

# from typing import NamedTuple

# class Paciente(NamedTuple):
#     nome: str
#     data_nascimento: str

#     def __str__(self):
#         return f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"
        

from dataclasses import dataclass

@dataclass(frozen=True)
class Paciente:
    nome: str
    data_nascimento: str

    def __str__(self):
        return f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"
    
    def calcular_idade(self) -> int:
        ano_nascimento = int(self.data_nascimento.split("/")[-1])
        ano_atual = 2025
        return ano_atual - ano_nascimento

    def maior_de_idade(self) -> bool:
        return self.calcular_idade() >= 18
    