s=input('Introduce sentence')
word=input('Introduce word')
lowercase_s=s.lower()
for i in lowercase_s:
    if not i.isalpha() and i!=' ':
        lowercase_s=lowercase_s.replace(i,'')
list_of_words=lowercase_s.split()  
count=0
for i in list_of_words:
    print(word,i)
    if word==i:
        count=count+1
print(count)