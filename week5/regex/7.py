import re

# s = input() 
s = "wdefsf_aefsgdfba_acdsv_cds_DSVF_w"
l = re.split(r"_", s)
s2 = ''
for i in l:
    s2 += (i[0].upper() + i[1:])
print(s2)