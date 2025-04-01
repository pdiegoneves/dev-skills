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
