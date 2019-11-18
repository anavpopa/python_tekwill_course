# Scrieti o functie care sa intoarca elementele distincte dintr-o lista

# Metoda 1
def eliminate_dupes(input_list):
    new_list=[]
    for i in input_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

# Metoda 2
def eliminate_dupes(input_list):
    new_list=[]
    s = set(input_list)
    input_list = list(s)
    print(input_list)



