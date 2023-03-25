import os 

path = '/Users/zeinaddinzurgambayev/pp2/week5'

for root,dire,files in os.walk(path):
    print (root)
    for d in dire:
        print(d)
    for f in files:
        print(f)