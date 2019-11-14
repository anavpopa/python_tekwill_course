#Exercitiul 4 (Scrieti un program care sa afiseze toti divizorii unui numar intreg)
n=int(input('Introduce integer'))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1