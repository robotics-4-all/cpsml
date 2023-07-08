from os.path import basename

from cpsml.utils import get_thing_mm, build_model


def dt2msg_name(name):
    return f'{name}Msg'


def build_sense_resource_uri(thing, sensor):
    uri = f'{thing.name.lower()}.sensors.{sensor.__class__.__name__.lower()}.{sensor.name.lower()}'
    return uri


def build_act_resource_uri(thing, actuator):
    uri = f'{thing.name.lower()}.actuators.{actuator.__class__.__name__.lower()}.{actuator.name.lower()}'
    return uri


def build_single_resource(name, rtype, interface, namespace='', uri='',
                          is_virtual=False):
    vtag = 'Virtual' if is_virtual else 'Physical'
    txt = f'Resource<{rtype}> {name}\n'
    txt += f'   uri: \'{uri}\'\n'
    txt += f'   interface: {interface}\n'
    txt += f"   namespace: '{namespace}'\n"
    txt += 'end\n\n'
    return txt


def build_thing_messages(thing):
    txt = ''
    dmodels_parsed = []
    for sensor in thing.sensors:
        dtype = sensor.dataModel
        if dtype in dmodels_parsed:
            continue
        dmodels_parsed.append(dtype)
        txt += f"TopicMsg {dtype.name}Msg\n"
        for p in dtype.properties:
            txt+= f'    {p.name}: {p.type}\n'
        txt += "end\n\n"
    for actuator in thing.actuators:
        dtype = actuator.dataModel
        if dtype in dmodels_parsed:
            continue
        dmodels_parsed.append(dtype)
        txt += f"TopicMsg {dtype.name}Msg\n"
        for p in dtype.properties:
            txt+= f'    {p.name}: {p.type}\n'
        txt += "end\n\n"
    return txt



def build_thing_resources(thing):
    txt = ''
    for sensor in thing.sensors:
        txt += build_single_resource(
            sensor.name, 'Sense',
            f'AsyncProducer<{dt2msg_name(sensor.dataModel.name)}>',
            uri=build_sense_resource_uri(thing, sensor)
        )
    for actuator in thing.actuators:
        txt += build_single_resource(
            actuator.name,
            'Act',
            f'AsyncConsumer<{dt2msg_name(actuator.dataModel.name)}>',
            uri=build_act_resource_uri(thing, actuator)
        )
    return txt


def log_thing_info(thing):
    print(f'[*] Installed Sensors:')
    for sensor in thing.sensors:
        print(f'- {sensor.name}: {sensor.__class__.__name__}')
    print(f'[*] Installed Actuators:')
    for actuator in thing.actuators:
        print(f'- {actuator.name}: {actuator.__class__.__name__}')
    print(f'[*] Installed Computation Boards:')
    for board in thing.boards:
        print(f'- {board}')


def build_resources_model_file(resources: str, filename='resources'):
    filepath = f'{filename}.resource'
    with open(filepath, 'w') as fp:
        fp.write(resources)
    return filepath


def t2r_m2m(thing_model, output_model=''):
    model_filename = basename(thing_model)
    if not model_filename.endswith('.thing'):
        print(f'[X] Not a thing model.')
        raise ValueError()
    mm = get_thing_mm()
    model = mm.model_from_file(thing_model)
    things = model.things
    for thing in things:
        log_thing_info(thing)
        msgs = build_thing_messages(thing)
        resources = build_thing_resources(thing)
        rmodel = msgs + resources
        model_filepath = build_resources_model_file(rmodel, thing.name)
        print(f'[*] Validating {thing.name} Resource model...')
        model = build_model(model_filepath)
        if model:
            print(f'[*] Validation passed!')
