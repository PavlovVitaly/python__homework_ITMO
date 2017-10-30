import datetime
import re
from abc import ABCMeta, abstractmethod


class ValidatorException(Exception):
    pass


class Validator(metaclass=ABCMeta):
    __VALIDATORS = {}

    @abstractmethod
    def validate(self, value):
        pass

    @classmethod
    def add_type(cls, name, validator):
        if not name:
            raise ValidatorException('Validator must have a name!')
        if not issubclass(validator, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(validator))
        cls.__VALIDATORS[name] = validator

    @classmethod
    def get_instance(cls, name):
        validator = cls.__VALIDATORS.get(name)
        if not validator:
            raise ValidatorException('Validator with name "{}" not found'.format(name))
        return validator()


class DateTimeValidator(Validator):
    def __init__(self):
        self.__pattern_of_date = list()
        self.__fill_out_pattern_of_date()

        self.__pattern_of_time = list()
        self.__fill_out_pattern_of_time()

    def __fill_out_pattern_of_date(self):
        self.__pattern_of_date.append([re.compile(r'\d{4}[-]\d{1,2}[-]\d{1,2}'), '-', [2, 1, 0]])
        self.__pattern_of_date.append([re.compile(r'\d{1,2}[.]\d{1,2}[.]\d{4}'), '.', [0, 1, 2]])
        self.__pattern_of_date.append([re.compile(r'\d{1,2}[/]\d{1,2}[/]\d{4}'), '/', [0, 1, 2]])

    def __fill_out_pattern_of_time(self):
        self.__pattern_of_time.append(re.compile(r'\d{2}[:]\d{2}'))
        self.__pattern_of_time.append(re.compile(r'\d{2}[:]\d{2}[:]\d{2}'))

    def validate(self, value):
        value = self.__get_list_of_date_nad_time(value)
        if not value:
            return False
        ret_val = self.__validate_date(value[0])
        if len(value) == 2:
            ret_val = ret_val and self.__validate_time(value[1])
        return ret_val

    def __get_list_of_date_nad_time(self, value):
        list_of_value = value.split()
        if len(list_of_value) > 2:
            return None
        for item in list_of_value:
            item.strip(' ')
        return list_of_value

    def __validate_date(self, value):
        for item in self.__pattern_of_date:
            if re.search(item[0], value):
                return self.__is_exist_date(value, item)
        return False

    def __is_exist_date(self, value, pattern):
        value = value.split(pattern[1])
        seq = pattern[2]
        value = list(map(int, value))
        day = value[seq[0]]
        month = value[seq[1]]
        year = value[seq[2]]
        try:
            datetime.date(year, month, day)
        except:
            return False
        return True

    def __validate_time(self, value):
        for item in self.__pattern_of_time:
            if re.search(item, value):
                return self.__is_exist_time(value)
        return False

    def __is_exist_time(self, value):
        value = value.split(':')
        value = list(map(int, value))
        hours = value[0]
        minutes = value[1]
        try:
            if len(value) == 3:
                seconds = value[2]
                datetime.time(hours, minutes, seconds)
            else:
                datetime.time(hours, minutes)
        except:
            return False
        return True


class EMailValidator(Validator):
    def __init__(self):
        self.__pattern_of_email = re.compile(r'\w+.\w+@\w+.\w+')
        self.__forbid_signs = [',', '!', '@', '#', '$', '^', '&', '*', '(', ')', '+', '=', "'"]

    def validate(self, value):
        if not re.search(self.__pattern_of_email, value):
            return False
        try:
            before_dog, after_dog = value.split('@')
            before_domen, domen = after_dog.split('.')
        except:
            return False
        if self.__is_consisted_forbid_signs(before_dog) or \
                self.__is_consisted_forbid_signs(after_dog) or \
                self.__is_consisted_forbid_signs(before_domen) or \
                self.__is_consisted_forbid_signs(domen):
            return False
        if before_dog.find('.') != before_dog.rfind('.'):
            return False
        return True

    def __is_consisted_forbid_signs(self, value):
        for item in self.__forbid_signs:
            if value.find(item) != -1:
                return True
        return False

# Validator.add_type('datetime', DateTimeValidator)
# Validator.add_type('email', EMailValidator)
#
# v = Validator.get_instance('datetime')
# print(v.validate('2017-09-01'))
# print(v.validate('01/10/2017 12:00'))
#
# vd = Validator.get_instance('email')
# print(vd.validate('info@itmo-it.org'))
# print(vd.validate('unknown'))
# print(vd.validate("!#$%&'*+.-/=?^_`{}|~@example.com"))
# print(vd.validate("Miles.O'Brian@example.com"))
# print(vd.validate('f.i.r.s.t.l.a.s.t@gmail.com'))
# print(vd.validate('allen+one@example.com'))
# print(vd.validate('postmaster@→→→→→→→.ws'))
# print(vd.validate('postmaster@xn--55gaaaaaa281gfaqg86dja792anqa.ws'))
# print(vd.validate('allen@[127.0.0.1]'))
# print(vd.validate(''))
