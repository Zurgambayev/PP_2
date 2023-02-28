

import re

s = input()

l = re.findall(r"[A-Z][a-z]*", s)
s1 = ''
for i in l:
    s1 += (i[0].lower() + i[1:] + '_')

print(s1[:-1])