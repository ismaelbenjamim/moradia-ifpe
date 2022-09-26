import os
from os.path import isfile, join

path = f"contrib/database/"
print(path)
onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
for file in onlyfiles:
    os.system(f"python manage.py loaddata contrib/database/{file}")