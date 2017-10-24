__READ = 'read'
__WRITE = 'write'


def read_params(source):
    read_func = __get_func(source, __READ)
    read_func(source)


def write_params(source, params):
    write_func = __get_func(source, __WRITE)
    write_func(source, params)


def __get_type_of_file(source):
    source = source.strip(' ').split('.')
    source = source[1]
    return source


def __get_func(source, purpose_of_func):
    type_of_file = __get_type_of_file(source)
    funcs = __FUNCTIONS.get(type_of_file)
    if not funcs:
        return None
    target_func = funcs.get(purpose_of_func)
    if not target_func:
        return None
    return target_func


def __read_txt(source):
    print('read_txt')


def __write_txt(source, params):
    print('write_txt')


def __read_json(source):
    print('read_json')


def __write_json(source, params):
    print('write_json')


def __read_xml(source):
    print('read_xml')


def __write_xml(source, params):
    print('write_xml')


def __read_ini(source):
    print('read_ini')


def __write_ini(source, params):
    print('write_ini')


__FUNCTIONS = {'txt': {'read': __read_txt,
                       'write': __write_txt},
               'json': {'read': __read_json,
                        'write': __write_json},
               'xml': {'read': __read_xml,
                       'write': __write_xml},
               'ini': {'read': __read_ini,
                       'write': __write_ini}}

f = '/params.txt'
f1 = '/params.json'

read_params(f)
write_params(f, 1)
read_params(f1)
write_params(f1, 1)
