codigo_ddi = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

codigo_ddi_dict = {nome_do_pais: codigo_ddi for codigo_ddi, nome_do_pais in codigo_ddi}


print("# DICT COMPREHENSIONS")
print(codigo_ddi)
print(codigo_ddi_dict)

print("# SORTED")
print(sorted(codigo_ddi_dict.items()))
print(sorted(codigo_ddi_dict.items(), key=lambda x: x[1]))

print("# DICT COMPREHENSION + SORTED")

print(

    {codigo: pais for pais, codigo in sorted(codigo_ddi_dict.items(), key=lambda x: x[1])}

)
print(

    {
        codigo: pais for pais, codigo in sorted(codigo_ddi_dict.items(), key=lambda x: x[1])
        if codigo < 70
     }

)


print("A partir do 3.9 '|' '|='")

d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

d2 = {
    'd': 4,
    'e': 5,
    'f': 6,
}

d3 = d1 | d2
print("D3", d3)

d1 |= d2
print("D1", d1)

print(" Hashable")

tupla1 = (1, 2, 3)
lista1 = [1, 2, 3]
tupla2 = (1, 2, 3)

print(hash(tupla1))
# print(hash(lista1)) unhashable
print(hash(tupla2))

class ClasseTeste():
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)
    
    def __eq__(self, other):
        return self.x == other.x



c1 = ClasseTeste(1)
c2 = ClasseTeste(1)

print(hash(c1))
print(hash(c2))

print(c1 == c2)