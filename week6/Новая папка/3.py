#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = input()
path1 = r'/Users/zeinaddinzurgambayev/pp2/week4'

if os.path.exists(path):
    x = os.path.split(path)
    print("Filename:", x[1])
    print("Directory portion:", x[0])
else:
    print("Path does not exists")
