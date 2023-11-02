from os.path import basename
import jinja2

from cpsml.lang import build_model
from cpsml.lang import get_entity_mm

from cpsml.utils import TEMPLATES_PATH


# Initialize template engine.
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    trim_blocks=True,
    lstrip_blocks=True
)

resources_tpl = jinja_env.get_template('entity_model.jinja')


def build_entity_model(context):
    modelf = resources_tpl.render(context)
    return modelf


def log_thing_info(thing):
    print(f'[*] Thing model: {thing.name}')
    print(f'[*] Installed Sensors:')
    for posed_sensor in thing.sensors:
        sensor = posed_sensor.ref
        print(f'- {sensor.name}: {sensor.__class__.__name__}')
    print(f'[*] Installed Actuators:')
    for posed_actuator in thing.actuators:
        actuator = posed_actuator.ref
        print(f'- {actuator.name}: {actuator.__class__.__name__}')
    if thing.__class__.__name__ == 'Robot':
        print(f'[*] Installed Computation Boards:')
        for posed_board in thing.boards:
            board = posed_board.ref
            print(f'- {board}')


def extract_entities(thing):
    sensors = []
    actuators = []
    # broker = thing.communication.name
    broker = thing.communication
    for psensor in thing.sensors:
        sensor = psensor.ref
        _cls = sensor.__class__.__name__.lower()
        uri = f'{thing.name.lower()}.sensors.{_cls}.{psensor.name.lower()}'
        attrs = []
        dm = sensor.dataModel
        for a in dm.properties:
            attrs.append((a.name, str(a.type)))
        _s = {
            'name': psensor.name,
            'type': 'sensor',
            'topic': uri,
            'broker': broker,
            'freq': sensor.pubFreq,
            'attributes': attrs
        }
        sensors.append(_s)
    for pactuator in thing.actuators:
        actuator = pactuator.ref
        _cls = actuator.__class__.__name__.lower()
        uri = f'{thing.name.lower()}.sensors.{_cls}.{pactuator.name.lower()}'
        attrs = []
        dm = actuator.dataModel
        for a in dm.properties:
            attrs.append((a.name, str(a.type)))
        _a = {
            'name': pactuator.name,
            'type': 'actuator',
            'topic': uri,
            'broker': broker,
            'attributes': attrs
        }
        actuators.append(_a)
    return {'sensors': sensors, 'actuators': actuators}


def thing_to_entity_m2m(thing):
    log_thing_info(thing)
    ent = extract_entities(thing)
    m = build_entity_model(ent)
    emm = get_entity_mm()
    emm.model_from_str(m)
    return m
