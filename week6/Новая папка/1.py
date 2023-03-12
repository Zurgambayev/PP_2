import os 

path = '/Users/zeinaddinzurgambayev/pp2/week5'

for root,directories,files in os.walk(path):
    print(root)
    for d in directories:
        print(d)
    for f in files:
        print(f)