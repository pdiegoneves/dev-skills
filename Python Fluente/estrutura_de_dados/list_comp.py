from timed import get_time
nums = range(1, 10)

@get_time
def test1():
    dobros = []
    for num in nums:
        dobros.append(num * 2)


    print(dobros)

@get_time
def test2():
    dobros2 = [num * 2 for num in nums]

    print(dobros2)


# test1()
# test2()



quadrados1 = (num * num for num in nums)
quadrados2 = [num * num for num in nums if num % 2 == 0]

print(quadrados1)
print(quadrados2)

naipes = ["Espadas", "Paus", "Copas", "Ouros"]
valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

cartas = [f"{valor} de {naipe}" for valor in valores 
                                for naipe in naipes]

print(cartas)