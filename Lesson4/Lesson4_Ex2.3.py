#Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o propozitie
s=input('Introduce sentence')
word=input('Introduce word in lowercase')
lowercase_s=s.lower()
new_s=lowercase_s.replace("'", " ")
replaced_s=new_s.replace("-", " ")
print(replaced_s)
for i in replaced_s:
    if not i.isalpha() and i!=' ':
        replaced_s=replaced_s.replace(i,'')
list_of_words=replaced_s.split()  
count=0
for i in list_of_words:
    if word==i:
        count=count+1
print(count)