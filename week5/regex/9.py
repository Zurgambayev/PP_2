import re
 

# with open("row.txt" , "rt") as file:
#     s = file.read().replace('\n', "").replace('\r', "")
s = input()
l = re.findall(r"[A-Z][a-z]*", s)
s1 = ''
for i in l:
    s1 += (i + ' ')

print(s1)