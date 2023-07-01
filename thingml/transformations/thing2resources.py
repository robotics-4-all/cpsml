from os.path import basename

from thingml.utils import get_thing_mm


def build_resource(name, rtype, interface, namespace='', uri=''):
    txt = f"""
    Resource<{rtype}> {name}
        'uri': '{uri}'
        'interface': {interface}
        'namespace': '{namespace}'
    end
    """
    print(txt)


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
            print(f'[*] Installed Sensors:')
            for sensor in thing.sensors:
                print(f'- {sensor.name}: {sensor.__class__.__name__}')
            print(f'[*] Installed Actuators:')
            for actuator in thing.actuators:
                print(f'- {actuator.name}: {actuator.__class__.__name__}')
            print(f'[*] Installed Computation Boards:')
            for board in thing.boards:
                print(f'- {board}')
            for sensor in thing.sensors:
                build_resource(sensor.name, 'Sense',
                               f'Publisher<{sensor.dataModel.name}>',
                               uri=f'{thing.name.lower()}.sensors.{sensor.name.lower()}'
                               )
            for actuator in thing.actuators:
                build_resource(actuator.name,
                               'Act',
                               f'Subscriber<{actuator.dataModel.name}>',
                               uri=f'{thing.name.lower()}.actuators.{actuator.name.lower()}'
                               )
            for cap in thing.capabilities:
                build_resource(cap,
                               'Compute',
                               f'Subscriber<{cap}>',
                               uri=f'{thing.name.lower()}.{cap.lower()}'
                               )
        elif thing.__class__.__name__ == 'Device':
            print(f'[*] Found {thing.__class__.__name__} model: {thing.name}')
