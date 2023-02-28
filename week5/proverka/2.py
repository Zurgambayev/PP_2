import re 

a = 'The rain in Spain'
x = re.search("^The.*Spain$",a)

if x:
  print("YES! We have a match!")
else:
  print("No match")