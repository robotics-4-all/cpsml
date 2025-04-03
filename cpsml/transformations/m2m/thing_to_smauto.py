from os.path import basename
import jinja2
from pydantic import BaseModel

from cpsml.lang import build_model
from cpsml.lang import get_entity_mm

from cpsml.utils import TEMPLATES_PATH


# Initialize template engine.
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    trim_blocks=True,
    lstrip_blocks=True
)

resources_tpl = jinja_env.get_template('smauto.jinja')


class Metadata(BaseModel):
    name: str = "CHANGE_ME"
    version: str = "0.1.0"
    author: str = "AUTHOR_NAME"
    email: str = "AUTHOR_EMAIL"
    description: str = "Add a description here"


def build_smauto_model(entities, brokers):
    sensors = entities['sensors']
    actuators = entities['actuators']
    # sensors = [ent for ent in entities if ent.etype == "sensor"]
    # actuators = [ent for ent in entities if ent.etype == "actuator"]
    # hybrids = [ent for ent in entities if ent.etype == "hybrid"]
    context = {
        'sensors': sensors,
        'actuators': actuators,
        'brokers': brokers,
        'metadata': Metadata()
    }
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
            'broker': broker.ref.name,
            'freq': sensor.pubFreq,
            'attributes': attrs
        }
        sensors.append(_s)
    for pactuator in thing.actuators:
        actuator = pactuator.ref
        _cls = actuator.__class__.__name__.lower()
        uri = f'{thing.name.lower()}.actuators.{_cls}.{pactuator.name.lower()}'
        attrs = []
        dm = actuator.dataModel
        name = pactuator.name or actuator.name
        for a in dm.properties:
            attrs.append((a.name, str(a.type)))
        _a = {
            'name': name,
            'type': 'actuator',
            'topic': uri,
            'broker': broker.ref.name,
            'attributes': attrs
        }
        actuators.append(_a)
    return {
        'sensors': sensors,
        'actuators': actuators
    }


def extract_broker(thing):
    broker_conn = thing.communication
    broker = list([broker_conn.ref]).copy()[0]
    if broker_conn.auth.username not in ("", None):
        broker.username = broker_conn.auth.username
    if broker_conn.auth.password not in ("", None):
        broker.password = broker_conn.auth.password
    return broker


def transform(thing):
    log_thing_info(thing)
    entities = extract_entities(thing)
    broker = extract_broker(thing)
    model_str = build_smauto_model(entities, [broker])
    return model_str
