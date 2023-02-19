from datetime import datetime

date_time = datetime(2023, 2, 15, 12, 30, 0)
formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date_time)