import re 
file = open('/Users/zeinaddinzurgambayev/pp2/week5/regex/row.txt','r')

result = file.read() 

Pattern = re.sub(r' ',',.', result)

print(Pattern)