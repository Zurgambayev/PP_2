import re
 

with open("row.txt" , "rt") as file:
    s = file.read().replace('\n', "").replace('\r', "")
s = str(s)
l = re.findall(r'[A-Z]{1}[a-z]+', s)

print(l)