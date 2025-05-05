# mutáveis
# list, bytearray, array.array e collections.deque

# imutáveis
# tuple, str, e bytes

import array
import collections
from collections import abc

print("MUTAVEL")
print("list", issubclass(list, abc.MutableSequence))
print("bytearray", issubclass(bytearray, abc.MutableSequence))
print("array", issubclass(array.array, abc.MutableSequence))
print("deque", issubclass(collections.deque, abc.MutableSequence))
print("MutableSequence", issubclass(abc.MutableSequence, abc.Sequence))

print("IMUTAVEL")
print("tuple", issubclass(tuple, abc.Sequence))
print("str", issubclass(str, abc.Sequence))
print("bytes", issubclass(bytes, abc.Sequence))


print("-----")
print("tuple", issubclass(tuple, abc.MutableSequence))
print("array", issubclass(array.array, abc.Sequence))


pessoas = [
    ("joao", 38),
    ("maria", 35),
    ("pedro", 40),
]


array_numeros = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
deque_numeros = collections.deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(pessoas)
print(array_numeros)
print(deque_numeros)


## Multabilidade

frutas = ["pera", "laranja", "banana", "maca"]

frutas[0] = "abacaxi"

print(frutas)


vogais = "aelou"
print(vogais[2])

vogais[2] = "i"  # TypeError: 'str' object does not support item assignment

print(vogais)
