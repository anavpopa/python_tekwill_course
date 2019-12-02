#  Ex1 Create new folder with name my_data_folder
#import os
#os.makedirs('C:\\Users\\user\\Documents\\Python\\Tekwill python\\L8\\my_data_folder')


#  Ex2 Change path to new created folder
import os
os.chdir('my_data_folder')
print(os.getcwd())


#Ex 3 Write in new created file following content with new line:
a=['Age', 'occupation', 'height']
with open('test.txt', 'w') as f:
    for i in a:
        f.write(f'{i}\n')
    f.close()

# Ex 4 Read file content and display it on screen
with open('test.txt') as f:
    data= f.read()
    print(data)
    f.close()

# Ex 5 Copy content of file created in ex. 3 in new file (open file in write mode)
with open('new_file.txt', 'w') as target:
    with open('test.txt') as source:
        data= source.read()
        source.close()
        target.write(data)
        target.close()



