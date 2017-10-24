class IConfigFile(object):
    def __init__(self, source='', params=''):
        self.__source = source
        self.__params = params
        self.__FUNCTIONS = dict()
        self.__READ = 'read'
        self.__WRITE = 'write'

    def set_source(self, source):
        self.__source = source

    def get_source(self):
        return self.__source

    def set_params(self, params):
        self.__params = params
        
    def get_params(self):
        return self.__params

    def read_params(self):
        read_func = self.__get_func(self.__READ)
        read_func()

    def write_params(self):
        write_func = self.__get_func(self.__WRITE)
        write_func()

    def __get_func(self, purpose_of_func):
        type_of_file = self.__get_type_of_file()
        funcs = self.__FUNCTIONS.get(type_of_file)
        if not funcs:
            return None
        target_func = funcs.get(purpose_of_func)
        if not target_func:
            return None
        return target_func

    def __get_type_of_file(self):
        source = self.__source.strip(' ').split('.')
        source = source[1]
        return source

    def add_fun(self, name, new_read_func, new_write_func):
        self.__FUNCTIONS[name] = {self.__READ: new_read_func,
                                  self.__WRITE: new_write_func}


class ConfigFileLite(IConfigFile):
    def __init__(self, source='', params=''):
        super().__init__(source=source, params=params)
        self.add_fun('txt', self.__read_txt, self.__write_txt)

    def __read_txt(self):
        print('read_txt')

    def __write_txt(self):
        print('write_txt')


class ConfigFileExp(ConfigFileLite):
    def __init__(self, source='', params=''):
        super().__init__(source=source, params=params)
        self.add_fun('json', self.__read_json, self.__write_json)
        self.add_fun('xml', self.__read_xml, self.__write_xml)
        self.add_fun('ini', self.__read_ini, self.__write_ini)

    def __read_json(self):
        print('read_json')

    def __write_json(self):
        print('write_json')

    def __read_xml(self):
        print('read_xml')

    def __write_xml(self):
        print('write_xml')

    def __read_ini(self):
        print('read_ini')

    def __write_ini(self):
        print('write_ini')


f = '/params.txt'
f1 = '/params.json'
lite = ConfigFileLite(f, 1)
exp = ConfigFileExp(f1, 1)

lite.read_params()
lite.write_params()

exp.read_params()
exp.write_params()

exp.set_source(f)

exp.read_params()
exp.write_params()
