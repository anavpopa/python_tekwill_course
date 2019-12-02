import os
total_size= 0
for filename in os.listdir('C:\\Users\\user\\Documents\\Python\\Tekwill python\\L8'):
    if filename.endswith('.py'):   # or use if os.path.splitext(filename)[-1]==".py":
        total_size=total_size+os.path.getsize(os.path.join('C:\\Users\\user\\Documents\\Python\\Tekwill python\\L8', filename))
print(total_size/1024)

