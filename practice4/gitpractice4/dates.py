"""
Date and time operations
"""

from datetime import datetime, timedelta


# 1. Current time
def get_current_time():
    return datetime.now()


# 2. Difference between two dates (in days)
def days_between(date1_str, date2_str, fmt="%Y-%m-%d"):
    """
    Calculate absolute difference in days between two dates.
    """
    date1 = datetime.strptime(date1_str, fmt)
    date2 = datetime.strptime(date2_str, fmt)
    return abs((date2 - date1).days)


# 3. Add days to a date
def add_days(date_str, days, fmt="%Y-%m-%d"):
    date = datetime.strptime(date_str, fmt)
    new_date = date + timedelta(days=days)
    return new_date.strftime(fmt)