class Pessoa:
    def __init__(self, nome):
        self.nome:str = nome

    def __new__(cls, nome):
        instancia  = super().__new__(cls) 
        instancia.dica = "Teste"
        print(f"Iniciando: {instancia.__class__.__name__}")
        return instancia 
    
    def __del__(self):
        print(f"Deletando {self.nome}")
    
    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"nome={self.nome!r}")
    
    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"nome={self.nome!r})")
    
    def __format__(self, formato):
        if formato == "formal":
            return f"Sr. {self}"
        
        return self.nome
    
    def __hash__(self):
        positions = ""
        for char in self.nome:
            positions += str(ord(char))
        return int(positions)
    
    def __bool__(self):
        return "P" in self.nome.upper()
    
    def __getattr__(self, nome_do_atributo):
        return f"{nome_do_atributo} não existe"
    
    def __getattribute__(self, name):
        print(f"Procurando o atributo {name}")
        return super().__getattribute__(name)
        
    
p = Pessoa("Diegop")
print(p.nome)
print(f"{2.1234567:.2f}")
print(f"{p:formal}")
print(p.dica)
print(p)
print(hash(p))

print(bool(p))
print(p.idade)

