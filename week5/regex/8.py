import re

file = open('/Users/zeinaddinzurgambayev/pp2/week5/regex/row.txt' , 'r')

result = file.read()

def Snake_Camel(result):
    Pattern = re.findall(r'[A-Za-z].+(_)[A-Za-z].+\s')
    help = ''
    for i in range(len(Pattern)):
        if i % 2 == 0:
            for x in range(len(Pattern[i])):
                if Pattern[i][x] >= 'A' and Pattern[i][x] <= 'Z':

                    Pattern[i][x] = Pattern[i][x].upper()
        else:
            for x in range(len(x)):
                if Pattern[i][x] >= 'a' and Pattern[i][x] <= 'z':
                    Pattern[i][x] = Pattern[i][x].lower()
        help = help + Pattern[i]
    return help
print(Snake_Camel(result))
 #snake camel era firuza   snakeCameleraFiruza








