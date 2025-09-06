print("Classe Simples")
class Coordinate:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

moscow = Coordinate(55.76, 37.62)
location = Coordinate(55.76, 37.62)
print(moscow)
print(location == moscow)
print((location.lat, location.lon) == (moscow.lat, moscow.lon))

print("Classe NamedTuple")

from collections import namedtuple

Coordinate2 = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate2, tuple))
moscow2 = Coordinate2(55.756, 37.617)
location2 = Coordinate2(55.756, 37.617)
print(moscow2)
print(location2 == moscow2)

print("Classe typing.NamedTuple")

import typing
Coordinate3 = typing.NamedTuple(
    'Coordinate', 
    [
        ('lat', float), 
        ('lon', float)
    ]
) 
print(issubclass(Coordinate3, tuple))
print(typing.get_type_hints(Coordinate3))
moscow3 = Coordinate3(55.756, 37.617)
location3 = Coordinate3(55.756, 37.617)
print(moscow3)
print(location3 == moscow3)



print("Classe typing.NamedTuple2")
class Coordinate4(typing.NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    

print(issubclass(Coordinate4, tuple))
print(typing.get_type_hints(Coordinate4))
moscow4 = Coordinate4(55.756, 37.617)
location4 = Coordinate4(55.756, 37.617)
print(moscow4)
print(location4 == moscow4)


print("Classe dataclasses")
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate5:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
print(issubclass(Coordinate5, tuple))
print(typing.get_type_hints(Coordinate5))
moscow4 = Coordinate5(55.756, 37.617)
location4 = Coordinate5(55.756, 37.617)
print(moscow4)
print(location4 == moscow4)