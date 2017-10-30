import os
from abc import ABCMeta, abstractmethod


class ParamHandlerException(Exception):
    pass


class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.__source = source
        self.__params = {}

    def add_param(self, key, value):
        self.__params[key] = value

    def set_param(self, params):
        self.__params = params

    def get_source(self):
        return self.__source

    def get_all_params(self):
        return self.__params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class ParamHandlerFactory(metaclass=ABCMeta):
    __types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))
        cls.__types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.__types.get(ext)
        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        return klass(source, *args, **kwargs)
