class Paciente():
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento


from collections import namedtuple
Paciente = namedtuple('Paciente', ['nome', 'data_nascimento'])

import typing

Paciente =   (
    'Paciente', 
    [
        ('nome', str), 
        ('data_nascimento', str)
    ]
)

import typing

class Paciente(typing.NamedTuple):
    nome: str
    data_nascimento: str

    def __str__(self):
        return f"{self.nome} nasceu em {self.data_nascimento}"

from dataclasses import dataclass

# @dataclass
@dataclass(frozen=True)
class Paciente:
    nome: str
    data_nascimento: str

    def __str__(self):
        return f"{self.nome} nasceu em {self.data_nascimento}"
    
    def calcular_idade(self):
        ano_nascimento = int(self.dada_nascimento.split('/')[2])
        ano_atual = 2025
        return ano_atual - ano_nascimento