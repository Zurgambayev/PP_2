# s = ["asd","asdf ","qefef"]
# a = [x.upper() for x in s]
# print(a)
"""
#  a = [x for x in range(10) if x < 5]
#  print(a)
"""
# a = ["apple", "banana", "cherry", "kiwi", "mango"]
# s = ["hello" for x in a] 

# print(s)


a =  ["apple", "banana", "cherry", "kiwi", "mango"]
s = [x if x != "banana" else "orange" for x in a]

print (s)