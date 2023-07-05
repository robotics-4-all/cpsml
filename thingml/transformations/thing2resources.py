from os.path import basename

from thingml.utils import get_thing_mm, build_model


class ResourceClasses:
    Sense = 'sensors'
    Act = 'actuators'
    Compute = 'compute'
    Storage = 'storage'


def build_sense_resource_uri(thing, sensor):
    uri = f'{thing.name.lower()}.sensors.{sensor.__class__.__name__.lower()}.{sensor.name.lower()}'
    return uri


def build_act_resource_uri(thing, actuator):
    uri = f'{thing.name.lower()}.actuators.{actuator.__class__.__name__.lower()}.{actuator.name.lower()}'
    return uri


def build_single_resource(name, rtype, interface, namespace='', uri='',
                          is_virtual=False):
    vtag = 'Virtual' if is_virtual else 'Physical'
    txt = f"""
    Resource<{rtype}> {name}
        uri: '{uri}'
        interface: {interface}
        namespace: '{namespace}'
        tags:
            - {vtag}
    end
    """
    return txt


def build_thing_resources(thing):
    print(f'[*] Installed Sensors:')
    for sensor in thing.sensors:
        print(f'- {sensor.name}: {sensor.__class__.__name__}')
    print(f'[*] Installed Actuators:')
    for actuator in thing.actuators:
        print(f'- {actuator.name}: {actuator.__class__.__name__}')
    print(f'[*] Installed Computation Boards:')
    for board in thing.boards:
        print(f'- {board}')
    txt = ''
    for sensor in thing.sensors:
        txt += build_single_resource(
            sensor.name, 'Sense',
            f'AsyncProducer<{sensor.dataModel.name}>',
            uri=build_sense_resource_uri(thing, sensor)
        )
    for actuator in thing.actuators:
        txt += build_single_resource(
            actuator.name,
            'Act',
            f'AsyncConsumer<{actuator.dataModel.name}>',
            uri=build_act_resource_uri(thing, actuator)
        )
    # for cap in thing.capabilities:
    #     txt += build_single_resource(
    #         cap,
    #         'Compute',
    #         f'Subscriber<{cap}>',
    #         uri=f'{thing.name.lower()}.{cap.lower()}'
    #     )
    return txt


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
        print('---------------------------------------')
        if thing.__class__.__name__ == 'Robot':
            print(f'[*] Found {thing.__class__.__name__} model: {thing.name}')
        elif thing.__class__.__name__ == 'Device':
            print(f'[*] Found {thing.__class__.__name__} model: {thing.name}')
        resources = build_thing_resources(thing)
        model_filepath = build_resources_model_file(resources, thing.name)
        print(f'[*] Validating {thing.name} Resource model...')
        model = build_model(model_filepath)
        if model:
            print(f'[*] Validation passed!')
