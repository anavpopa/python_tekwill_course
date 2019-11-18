#Scrieti o functie care primeste la input un text cu cifre si il converteste numar, 
# in caz de exceptie (este introdus o litera), afisati un mesaj de erroare si chemati functia de convertire din nou.
 
no=input('Introduce number')

def convert(str):
    try:
        n=int(str)
        print(n)
    except ValueError:
        print("EROOR: Cannot convert")
        convert(input('Introduce number again'))

convert(no)

