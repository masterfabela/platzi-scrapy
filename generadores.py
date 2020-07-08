# Funcion normal
def my_function():
    a = 1
    return a
    a = 2
    return a
    a = 3
    return a

# print(my_function())

# Generador (Recuerda el estado despues de ser llamada)
def my_generator():
    a = 1
    yield a
    a = 2
    yield a
    a = 3
    yield a

my_first_generator = my_generator()
# print(next(my_first_generator))
# print(next(my_first_generator))
# print(next(my_first_generator))

# Construir generador que retorne los 100 primeros numeros pares
def first_pairs():
    count = 1
    while(count <= 100):
        yield 2*count
        count = count+1

iterador_cien_pares = first_pairs()
print(next(iterador_cien_pares))
print(next(iterador_cien_pares))
print(next(iterador_cien_pares))
print(next(iterador_cien_pares))
print(next(iterador_cien_pares))