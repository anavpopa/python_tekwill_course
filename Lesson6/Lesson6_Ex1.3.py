# Scrieti o functie care sa calculeze numarul de litere majuscule si minuscule dintr-un text

def upper_lower_case(s):
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
            upper_case=upper_case+1
        elif i.islower():
            lower_case=lower_case+1
    return upper_case, lower_case
print(upper_lower_case("Top English School of Today"))