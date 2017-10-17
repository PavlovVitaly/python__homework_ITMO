import Notebook.notebook.validation_datetime as pac_valid_dt


def input_name_of_task():
    name_of_task = input('Введите имя задачи:')
    return name_of_task


def input_description_of_task():
    description_of_task = input('Введите описание задачи:')
    return description_of_task


def input_date_of_start_of_task():
    while True:
        date_of_start = input('Введите дату начала задачи в формате дд.мм.гггг '
                              '(для установки текущей даты оставте пустую строку и нажмите Enter):')
        if date_of_start is '':
            break
        if not pac_valid_dt.is_valid_date(date_of_start):
            print('Некорректный ввод даты')
            continue

    return date_of_start
