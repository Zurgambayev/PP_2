import re
 

with open("row.txt" , "rt") as file:
    s = file.read().replace('\n', "").replace('\r', "")
s = str(s)
l = re.findall(r'[a-zA-Z]*a[a-zA-Z]*b', s)

print(l)