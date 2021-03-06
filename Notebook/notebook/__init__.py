import sys

import Notebook.notebook.add_new_task_action as add_new_task

TEXT_OF_MAIN_MENU = {
    'HEAD_TEXT_OF_MAIN_MENU': 'Ежедневник. Выберите действие:\n\n',
    'LIST_OF_TASKS': '1. Вывести список задач\n',
    'ADD_TASK': '2. Добавить задачу\n',
    'EDIT_TASK': '3. Отредактировать задачу\n',
    'CLOSE_TASK': '4. Завершить задачу\n',
    'REINIT_TASK': '5. Начать задачу сначала\n',
    'SHOW_MENU': 'm. Покзать меню',
    'EXIT': 'q. Выход\n'
}

MSG_OF_MAIN_MENU = TEXT_OF_MAIN_MENU['HEAD_TEXT_OF_MAIN_MENU'] + \
                   TEXT_OF_MAIN_MENU['LIST_OF_TASKS'] + \
                   TEXT_OF_MAIN_MENU['ADD_TASK'] + \
                   TEXT_OF_MAIN_MENU['EDIT_TASK'] + \
                   TEXT_OF_MAIN_MENU['CLOSE_TASK'] + \
                   TEXT_OF_MAIN_MENU['REINIT_TASK'] + \
                   TEXT_OF_MAIN_MENU['EXIT']


def __list_of_tasks():
    print(TEXT_OF_MAIN_MENU.get('LIST_OF_TASKS'))


def __action_add_task():
    name_of_task = add_new_task.input_name_of_task()
    description_of_task = add_new_task.input_description_of_task()
    date_of_start = input('Введите дату начала задачи в формате дд.мм.гггг '
                          '(для установки текущей даты оставте пустую строку и нажмите Enter):')
    time_of_start = input('Введите время начала задачи в формате чч:мм (24-часовой формат времени)'
                          '(для установки "00:00", оставте пустую строку и нажмите Enter):')
    date_of_end = input('Введите дату окончания задачи в формате дд.мм.гггг'
                        ' (для установки текущей даты оставте пустую строку и нажмите Enter):')
    time_of_end = input('Введите время окончания задачи в формате чч:мм (24-часовой формат времени)'
                        '(для установки "00:00", оставте пустую строку и нажмите Enter):')


def __action_edit_task():
    print(TEXT_OF_MAIN_MENU.get('EDIT_TASK'))


def __action_close_task():
    print(TEXT_OF_MAIN_MENU.get('CLOSE_TASK'))


def __action_reinit_task():
    print(TEXT_OF_MAIN_MENU.get('REINIT_TASK'))


def __action_show_menu():
    print(MSG_OF_MAIN_MENU)


def __action_exit_from_program():
    print(TEXT_OF_MAIN_MENU.get('EXIT'))
    sys.exit()


MENU_OPTION = {
    '1': __list_of_tasks,
    '2': __action_add_task,
    '3': __action_edit_task,
    '4': __action_close_task,
    '5': __action_reinit_task,
    'm': __action_show_menu,
    'q': __action_exit_from_program
}


def main():
    __action_show_menu()
    while True:
        action = MENU_OPTION.get(input())
        if action:
            action()
        else:
            print('Неизвестная команда')
