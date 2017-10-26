from OOP_conf_file.pickle_json import ParamHandlerFactory

source_pickle = 'PICKLE_RICK.pickle'
pickle_Rick = ParamHandlerFactory.get_instance(source_pickle)
pickle_Rick.add_param('Pickle', 'Rick')
pickle_Rick.write()
pickle_Rick.read()
print(pickle_Rick.get_all_params())

source_json = 'JSON.json'
guano_apes = ParamHandlerFactory.get_instance(source_json)
guano_apes.add_param('Lose', 'Yourself')
guano_apes.write()
guano_apes.read()
print(guano_apes.get_all_params())
