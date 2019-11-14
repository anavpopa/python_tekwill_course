#Exercitiul 5 (Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest la 5 si 7)
sum=0
n=1000
while n<=2300:
    if n%5==0 and n%7==0:
        sum=sum+n
    n=n+1
print(sum)