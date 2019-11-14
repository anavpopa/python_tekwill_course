#Exercitiul 2 (F to C)
temperature = input("Enter temperature in F or C")
temp = int(temperature[0:-1])
if temperature[-1]=='F':
   print(str((temp-32)*5/9)+'C')
if temperature[-1]=='C':
   print(str(temp*9/5+32)+'F')
else:
   print('ERROR: No measurment specified')