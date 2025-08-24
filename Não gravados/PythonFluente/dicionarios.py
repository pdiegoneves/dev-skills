codigo_ddi = [
    (880, 'Bangladesh'),
    (55,  'Brazil'),
    (86,  'China'),
    (91,  'India'),
    (62,  'Indonesia'),
    (81,  'Japan'),
    (234, 'Nigeria'),
    (92,  'Pakistan'),
    (7,   'Russia'),
    (1,   'United States'),
]

codigo_ddi_dict = {pais: codigo for codigo, pais in codigo_ddi}

print(codigo_ddi)
print(codigo_ddi_dict)

print(sorted(codigo_ddi_dict, key=lambda x: x[1]))

print(
    {codigo: pais for pais, codigo in sorted(codigo_ddi_dict.items(), key=lambda x: x[1])}
)
print(
    {codigo: pais for pais, codigo in sorted(codigo_ddi_dict.items(), key=lambda x: x[1])
    if codigo < 70}
)

print(
    {codigo: pais.upper() for pais, codigo in sorted(codigo_ddi_dict.items(), key=lambda x: x[1])
    if codigo < 70}
)


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

print(d1 | d2)


d3 = {'g': 7}

d3 |= d1
d3 |= d2

print(d3)

## Hashble

tupla1 = (1,2,3,4)
lista = [1,2,3,4]
tupla2 = (1,2,3,4)

print(hash(tupla1))
# print(hash(l))
print(hash(tupla2))

print(tupla1 == tupla2)


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