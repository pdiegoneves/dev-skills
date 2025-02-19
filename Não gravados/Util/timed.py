#coding: utf-8
import time
import logging

def get_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Função: {func.__name__}\nTempo de execução: {end - start:.6f} segundos")
        return result
    return wrapper

