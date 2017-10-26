import json
import pickle

from OOP_conf_file.ParamHandler import ParamHandler, ParamHandlerFactory


class PickleParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
        with open(self.get_source(), 'rb') as f:
            self.set_param(pickle.load(f))

    def write(self):
        with open(self.get_source(), 'wb') as f:
            pickle.dump(self.get_all_params(), f)


class JsonParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
        with open(self.get_source(), 'r', encoding='UTF-8') as f:
            self.set_param(json.load(f))

    def write(self):
        with open(self.get_source(), 'w', encoding='UTF-8') as f:
            f.write(json.dumps(self.get_all_params(), ensure_ascii=False))


ParamHandlerFactory.add_type('pickle', PickleParamHandler)
ParamHandlerFactory.add_type('json', JsonParamHandler)
