#Exercitiul 3 (palindrom) Metoda 1
expression=input('introduce expression')
backwards=expression[::-1]
if expression==backwards:
    print('Palindrome')
else:
    print('Not palindrome')

#Exercitiul 3 (palindrom) Metoda 2
s = input('Introduce expression')
i = 0
is_palindrome = True
while i<int(len(s)/2):
    if (s[i] != s[-1-i]):
        is_palindrome= False
        break
    i+=1
if is_palindrome == True:
    print('Palindrome')
else:
    print('Not palindrome')