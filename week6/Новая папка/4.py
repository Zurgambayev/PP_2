#Write a Python program to count the number of lines in a text file.
import os

path = r'/Users/zeinaddinzurgambayev/pp2/week1,2 '

file = open(path, 'rt')

cnt = 0
while file.readline():
    cnt += 1

print(cnt)