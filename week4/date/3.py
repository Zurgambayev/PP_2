import datetime

today = datetime.date.today()
print("Current date:", today)
for i in range(5):
    a = today - datetime.timedelta(i + 1)
    print("Subtracting", i + 1 , "days gives us:", a)