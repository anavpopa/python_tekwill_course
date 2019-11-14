#Scrieti un program care sa calculeze numarul de litere si cifre din un text
str=input('Introduceti textul')
digit=0
letter=0
i=0
for i in range(len(str)):
    if str[i].isnumeric():
        digit=digit+1
        i=i+1
    elif str[i].isalpha():
        letter=letter+1
        i=i+1
    else:
        i=i+1
print(digit)
print(letter)