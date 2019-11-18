# Scrieti o functie care calculeaza daca un numar este prim

def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print('Not prime')
                break
        else:
            print('Prime')
prime(7)
