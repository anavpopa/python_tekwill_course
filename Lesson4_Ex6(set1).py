n=int(input('Introduce integer'))
i=2
Dict={1:1}
while i<=n:
    x={i:i**2}
    Dict.update(x)
    i=i+1
print(Dict)