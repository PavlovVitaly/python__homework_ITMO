import datetime

import Notebook.notebook.format_of_input_line as pac_for_format

__VALID_NUMBERS_PART_OF_DATE = 3
__VALID_NUMBERS_PART_OF_TIME = 2


def is_valid_date(date):
    try:
        start_date = convert_str_to_date(date)
    except ValueError:
        return False
    except:
        return False

    if __is_later_than_now(start_date):
        return False

    return True


def convert_str_to_date(date):
    separate_date = pac_for_format.format_the_line(date)
    separate_date = separate_date.split(".")

    if not __is_valid_numbers_of_part(separate_date, __VALID_NUMBERS_PART_OF_DATE):
        raise ValueError

    try:
        separate_date = list(map(int, separate_date))
        ret_date = datetime.date(separate_date[2], separate_date[1], separate_date[0])
    except ValueError:
        raise ValueError
    except:
        raise ValueError

    return ret_date


def __is_valid_numbers_of_part(separate_date, num_of_part):
    if len(separate_date) != num_of_part:
        return False
    return True


def __is_later_than_now(start_date):
    return is_later_than_start_date(start_date, datetime.datetime.now().date())


def is_later_than_start_date(end_date, start_date):
    dif_of_date = (end_date - start_date).days
    if dif_of_date < 0:
        return True
    return False


def convert_str_to_time(time):
    separate_time = pac_for_format.format_the_line(time)
    separate_time = separate_time.split(":")

    if __is_valid_numbers_of_part(separate_time, __VALID_NUMBERS_PART_OF_TIME):
        raise ValueError

    separate_time = list(map(int, separate_time))
    ret_time = datetime.time(separate_time[0], separate_time[1])
    return ret_time


def is_valid_time(time):
    try:
        converted_time = convert_str_to_date(time)
    except ValueError:
        return False
    except:
        return False

    return True


def get_date(date):
    return convert_str_to_date(date)


def create_datetime(date, time):
    return datetime.datetime.combine(date, time)


def is_valid_time_interval(datetime_of_start, datetime_of_end):
    if (datetime_of_end - datetime_of_start).total_seconds() >= 0:
        return True
    return False
