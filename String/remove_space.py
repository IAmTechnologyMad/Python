import re

c  =  "GfG is good         website"

s = re.sub(' +', ' ', c)

print(s)