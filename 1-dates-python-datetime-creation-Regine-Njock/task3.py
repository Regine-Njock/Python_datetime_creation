from datetime import datetime
from datetime import timedelta


def is_leap_year(year):
    dt = datetime(year, 2, 1)
    delta = timedelta(days=28)
    dt = dt + delta
    if dt.month == 2:
        return f'{year} is a leap year'
    return f'{year} is not a leap year'
print(is_leap_year(2021))