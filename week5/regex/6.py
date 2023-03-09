

import re
 

with open("row.txt" , "rt") as file:
    s = file.read().replace('\n', "").replace('\r', "")
s = str(s)
l = re.sub("\.+",":", s)
l = re.sub("[ ]",",", s)
print(l)


#Adsfgg [A-Z]{1}[a-z]8*