# Scrieti o functie care sa calculeze produsul elementelor unei liste

# Metoda1
def product(input_list):
    prod=1
    for i in input_list:
        prod=prod*i
    return prod

# Metoda 2
def multiply_list(*args):
    a=1
    for i in args:
        a=a*i
    return a
print(multiply_list(1,2,3,4))