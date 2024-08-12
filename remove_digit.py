import re

n = 'Geeks42eeks' 

for i in n:
    r = re.sub(r'[0-9]+', '',n)
print(r)