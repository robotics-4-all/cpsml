from os.path import basename

from cpsml.lang import build_model
from cpsml.lang import get_thing_mm

from cpsml.utils import TEMPLATES_PATH

import jinja2

# Initialize template engine.
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    trim_blocks=True,
    lstrip_blocks=True
)

resources_tpl = jinja_env.get_template('t2r.jinja')


def build_resources_model(thing, tags):
    context = {
        'thing': thing,
        'tags': tags,
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


def thing_to_resources_m2m(thing) -> str:
    log_thing_info(thing)
    rmodel_str = build_resources_model(thing, [])
    return rmodel_str
