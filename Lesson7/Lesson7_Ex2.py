def pow_of_n(n):
    while n>0:
        print(n)
        yield n*n
        n=n-1
for i in pow_of_n(10):
    print(i)