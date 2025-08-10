import time


def get_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} EXECUTADO EM: {end - start:.6f} segundos")
        return result

    return wrapper


if __name__ == "__main__":

    @get_time
    def test():
        print("Teste")
        print("Teste")
        print("Teste")
        print("Teste")

    test()
