import os 

path = input()

if os.path.exists(path):
    put,directories = os.path.split(path)
    print('Path', put)
    print('Direc',directories)
else:
    print('None')