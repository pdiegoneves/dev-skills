from timed import get_time
nums = range(1, 1_500_000)

print(f'Executando com {len(nums)} elementos')

@get_time
def dobrar():
    dobro = []
    for num in nums:
        dobro.append(num * 2)
    
    # print(dobro)

@get_time
def dobrar2():
    dobro2 = [num * 2 for num in nums]
    # print(dobro2)

suits = ["Espadas", "Paus", "Copas", "Ouros"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cards = [value + " " + suit for value in values 
                      for suit in suits]

print(cards)

dobrar()
dobrar2()


nums2 = range(1, 20)

squares = {}


for num in nums2:
    squares[num] = num * num

# squares = [num * num for num in nums2]

squares = list(num * num for num in nums2)

# squares = {num : num * num for num in nums}

# squares = {num : num * num for num in nums2 if num % 2 == 0}

print(squares)