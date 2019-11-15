# Scrieti un program care verifica daca o parola introdusa de utilizator este securizata
password=input('Introduceti parola')
special_characters=['!','/','#']
forbidden_characters=['@',"'",'{','}']
validity=True

if len(password)<6:
    validity=False
if not any(i.isupper() for i in password):
    validity=False
if not any(i.islower() for i in password):
    validity=False
if not any(i.isnumeric() for i in password):
    validity=False
if not any(i in special_characters for i in password):
    validity=False
if any(i in forbidden_characters for i in password):
    validity=False
if validity:
    print('Password is valid')
else:
    print('Password not valid')



