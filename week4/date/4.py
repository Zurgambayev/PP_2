
import datetime

current_datetime = datetime.datetime.now()
new_datetime = current_datetime.replace(microsecond=0)

print("Current datetime:", current_datetime)
print("New datetime:", new_datetime)
