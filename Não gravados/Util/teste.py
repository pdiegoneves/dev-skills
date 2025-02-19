from timed import get_time

@get_time
def fatorial(n:float):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial


print(fatorial(100))