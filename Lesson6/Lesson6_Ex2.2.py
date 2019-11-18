#Scrieti o functie care afiseaza o secventa de numere Fibonacci

#Metoda 1
n = input('Enter integer number')
def fibonacci(n):
    if n <= 1:
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))

for i in range(int(n)):
    print(fibo(i), end=', ')

#Metoda 2
n = input('Enter integer number')
def fibonacci(n):
    if n <= 1:
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))
l=[]
for i in range(int(n)):
    l.append(fibonacci(i))
print(l)


