from os.path import basename

from cpsml.lang import get_resource_mm, build_model
from cpsml.utils import TEMPLATES_PATH

import jinja2

# Initialize template engine.
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    trim_blocks=True,
    lstrip_blocks=True
)

api_tpl = jinja_env.get_template('api_model.jinja')


def build_api_model_file(context, filename='myapi'):
    filepath = f'{filename}.api'
    modelf = api_tpl.render(
        context
    )
    with open(filepath, 'w') as fp:
        fp.write(modelf)


def resource_to_endpoint(resource):
    iface = resource.interface
    msg = iface.msg
    etype = ''
    if iface.__class__.__name__ == 'AsyncConsumer':
        etype = 'subscriber'
    elif iface.__class__.__name__ == 'AsyncProducer':
        etype = 'publisher'
    else:
        # TODO
        raise ValueError()
    e = {
        'type': etype,
        'uri': resource.uri,
        'msg': msg,
        'namespace': resource.namespace
    }
    return e, msg


def r2api_m2m(resource_model_path: str, output_model=''):
    model_filename = basename(resource_model_path)
    if not model_filename.endswith('.resource'):
        print(f'[X] Not a resource model.')
        raise ValueError()
    mm = get_resource_mm()
    model = mm.model_from_file(resource_model_path)
    resources = model.resources
    print(f'[*] Found {len(resources)} Resources')
    print(f'[*] {resources}')

    broker = {
        'type': 'MQTT',
        'host': 'localhost',
        'port': 1883
    }
    endpoints = []
    msgs = []
    for r in resources:
        e, msg = resource_to_endpoint(r)
        endpoints.append(e)
        msgs.append(msg)
        print(msg.__class__.__name__)
    context = {
        'broker': broker,
        'endpoints': endpoints,
        'msgs': msgs
    }
    build_api_model_file(context)
