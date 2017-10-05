import datetime


def get_days_to_new_year():
    new_year_date = datetime.date(datetime.datetime.now().year + 1, 1, 1)
    days_remained = (new_year_date - datetime.datetime.now().date()).days
    return days_remained
