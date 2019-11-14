s=input('Introduce sentence')
l=s.split()
print(l)
new_list=[]
for i in l:
    if i not in new_list:
        new_list.append(i)
print(new_list)
new_string=' '.join(new_list)
print(new_string)