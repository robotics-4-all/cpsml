from os.path import basename

from cpsml.lang import build_model
from cpsml.lang import get_thing_mm


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


def thing_to_resources_m2m(thing) -> str:
    log_thing_info(thing)
    msgs = build_thing_messages(thing)
    resources = build_thing_resources(thing)
    rmodel_str = msgs + resources
    return rmodel_str
