from datetime import datetime

date_as_string = "Feb 14 2021 8:30AM"
dt = datetime.strptime(date_as_string, '%b %d %Y %I:%M%p')
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
