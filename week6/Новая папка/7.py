#Write a Python program to copy the contents of a file to another file
import os 

init_file = open(r'/Users/zeinaddinzurgambayev/pp2/week5', 'rt')

init_read = init_file.read()

final_file = open(r'/Users/zeinaddinzurgambayev/pp2/week5', 'wt')

final_file.write(init_read)