import datetime

__VALID_NUMBERS_PART_OF_DATE = 3


def format_the_line(line):
    line = line.replace('\n', '').strip(' ')
    return line


def is_valid_date(date):
    separate_date = format_the_line(date)
    separate_date = separate_date.split(".")

    if __is_not_valid_numbers_of_part_of_date(separate_date):
        return False

    try:
        start_date = datetime.date(separate_date[2], separate_date[1], separate_date[0])
    except ValueError:
        return False

    if __is_later_than_now(start_date):
        return False

    return True


def __is_not_valid_numbers_of_part_of_date(separate_date):
    if len(separate_date) != __VALID_NUMBERS_PART_OF_DATE:
        return True
    return False


def __is_later_than_now(start_date):
    dif_of_date = (start_date - datetime.datetime.now().date()).days
    if dif_of_date < 0:
        return True
    return False
