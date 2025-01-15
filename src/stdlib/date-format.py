from datetime import datetime

now = datetime.now()
formated_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formated_date)
