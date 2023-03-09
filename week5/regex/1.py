import re 

file = open('/Users/zeinaddinzurgambayev/pp2/week5/regex/row.txt', 'r')
contents = file.read()
result = re.findall('ab+',contents)
print(result)

