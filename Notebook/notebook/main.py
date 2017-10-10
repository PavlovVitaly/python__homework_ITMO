TEXT_OF_MAIN_MENU = {
    'HEAD_TEXT_OF_MAIN_MENU': 'Ежедневник. Выберите действие:\n\n',
    'LIST_OF_TASKS': '1. Вывести список задач\n',
    'ADD_TASK': '2. Добавить задачу\n',
    'EDIT_TASK': '3. Отредактировать задачу\n',
    'CLOSE_TASK': '4. Завершить задачу\n',
    'REINIT_TASK': '5. Начать задачу сначала\n',
    'EXIT': '6. Выход\n',
}


def __list_of_tasks():
    print(TEXT_OF_MAIN_MENU['LIST_OF_TASKS'])


def __add_task():
    print(TEXT_OF_MAIN_MENU['ADD_TASK'])


def __edit_task():
    print(TEXT_OF_MAIN_MENU['EDIT_TASK'])


def __close_task():
    print(TEXT_OF_MAIN_MENU['CLOSE_TASK'])


def __reinit_task():
    print(TEXT_OF_MAIN_MENU['REINIT_TASK'])


def __exit_from_program():
    print(TEXT_OF_MAIN_MENU['EXIT'])
    exit()


MENU_OPTION = {
    '1': __list_of_tasks,
    '2': __add_task,
    '3': __edit_task,
    '4': __close_task,
    '5': __reinit_task,
    '6': __exit_from_program
}


def main():
    while (True):
        print(TEXT_OF_MAIN_MENU['HEAD_TEXT_OF_MAIN_MENU'],
              TEXT_OF_MAIN_MENU['LIST_OF_TASKS'],
              TEXT_OF_MAIN_MENU['ADD_TASK'],
              TEXT_OF_MAIN_MENU['EDIT_TASK'],
              TEXT_OF_MAIN_MENU['CLOSE_TASK'],
              TEXT_OF_MAIN_MENU['REINIT_TASK'],
              TEXT_OF_MAIN_MENU['EXIT'])
        MENU_OPTION[input()]()


main()
