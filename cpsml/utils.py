from os.path import dirname, join, basename


THIS_DIR = dirname(__file__)
MODEL_REPO_PATH = join(THIS_DIR, '..', 'models')
TEMPLATES_PATH = join(THIS_DIR, 'templates')


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
