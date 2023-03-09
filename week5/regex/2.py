import re 

file = open('/Users/zeinaddinzurgambayev/pp2/week5/regex/row.txt','r')

consider = file.read()
Pattern = re.findall('ab{2,3}',consider)
print(Pattern)
