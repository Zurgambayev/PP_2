import re 

file = open('/Users/zeinaddinzurgambayev/pp2/week5/regex/row.txt','r')

result = file.read()

Pattern = re.findall('.*[a-z]-[a-z].*',result)

print(Pattern)