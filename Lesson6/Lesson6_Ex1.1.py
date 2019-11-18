# Scrieti o functie care sa gaseasca maximum a 3 numere

def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(biggest(3,7,34))