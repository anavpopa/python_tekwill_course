# Find name of last modified file in your current working directory.
import os
files = os.scandir('C:\\Users\\user\\Documents\\Python\\Tekwill python\\L8')
d={}
for f in files:
    if os.path.isfile(f)==True:
        d.update({os.path.basename(f): os.path.getmtime(f)})
lattest_modified=max(d, key=d.get)
print(lattest_modified)

