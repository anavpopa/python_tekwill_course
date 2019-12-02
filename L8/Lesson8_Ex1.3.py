import os
files = os.scandir('C:\\Users\\user\\Documents\\Python\\Tekwill python\\L8')
d={}
for f in files:
    if os.path.isfile(f)==True:
        d.update({os.path.basename(f): os.path.getatime(f)})
lattest_accessed=max(d, key=d.get)
print(lattest_accessed) 