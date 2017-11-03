from abc import ABCMeta, abstractmethod


class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


def is_valid_type(klass, type_of_klass):
    if not issubclass(klass, type_of_klass):
        return False
    else:
        return True


def return_fn_or_throw_exception(fn, klass, type_of_base_klass, type_of_exception):
    if not is_valid_type(klass, type_of_base_klass):
        raise type_of_exception('Class "{}" is not Command!'.format(klass))
    else:
        return fn


def check_type_of_argument(type_of_base_klass, type_of_exception):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            klass_kwargs = kwargs.get('klass')
            if klass_kwargs:
                res_fn = return_fn_or_throw_exception(fn, klass_kwargs, type_of_base_klass, type_of_exception)
            else:
                klass_args = args[2]
                res_fn = return_fn_or_throw_exception(fn, klass_args, type_of_base_klass, type_of_exception)
            return res_fn(*args, **kwargs)

        return wrapper

    return decorator


def check_name_arg(type_of_exception):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            name_kwargs = kwargs.get('name')
            if not (name_kwargs is None):
                if not name_kwargs:
                    raise type_of_exception('Command must have a name!')
            else:
                name_args = args[1]
                if not name_args:
                    raise type_of_exception('Command must have a name!')
            return fn(*args, **kwargs)

        return wrapper

    return decorator


class Menu(object):
    def __init__(self):
        self.__commands = {}
        self.__cur_commands = -1

    @check_name_arg(CommandException)
    @check_type_of_argument(Command, CommandException)
    def add_command(self, name, klass):
        storage_class = self.__commands.get(name)
        if storage_class is None:
            self.__commands[name] = klass

    def execute(self, name, *args, **kwargs):
        storage_class = self.__commands.get(name)
        if storage_class is None:
            raise CommandException('Command with name "{}" not found'.format(name))
        comm = storage_class(*args, **kwargs)
        return comm.execute()

    def __iter__(self):
        if len(self.__commands.items()) > 0:
            self.__cur_commands = 0
        else:
            self.__cur_commands = - 1
        return self

    def __next__(self):
        if self.__cur_commands < 0 or self.__cur_commands >= len(self.__commands.items()):
            raise StopIteration('No more elements')
        ret_val = (list(self.__commands.items()))[self.__cur_commands]
        self.__cur_commands += 1
        return ret_val


if __name__ == '__main__':

    class C1(Command):
        def execute(self):
            print('C1')


    class C2(Command):
        def execute(self):
            print('C1')


    class C3(Command):
        def execute(self):
            print('C1')


    menu = Menu()
    menu.add_command('c1', C1)
    menu.add_command('c2', C2)
    menu.add_command('c3', C3)
    print('ok')

    for name, command in menu:
        print(name, command)
        menu.execute(name)
