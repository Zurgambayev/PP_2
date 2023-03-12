#Write a Python program to write a list to a file.
import os

path = r'/Users/zeinaddinzurgambayev/pp2/week4'

file = open(path, 'wt')

list = ["Write ", "a ", "Python ", "program ", "to ", "write ", "a ", "list ", "to ", "a ", "file."]

for i in list:
    file.write(i)