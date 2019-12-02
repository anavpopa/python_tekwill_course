#  Ex1
#import os
#os.makedirs('C:\\Users\\user\\Documents\\Python\\Tekwill python\\L8\\my_data_folder')


#  Ex2
import os
os.chdir('my_data_folder')
print(os.getcwd())


#Ex 3
a=['Age', 'occupation', 'height']
with open('test.txt', 'w') as f:
    for i in a:
        f.write(f'{i}\n')
    f.close()

# Ex 4
with open('test.txt') as f:
    data= f.read()
    print(data)
    f.close()

# Ex 5
with open('new_file.txt', 'w') as target:
    with open('test.txt') as source:
        data= source.read()
        source.close()
        target.write(data)
        target.close()



