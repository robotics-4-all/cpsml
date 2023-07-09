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

api_tpl = jinja_env.get_template('r2api.jinja')


def build_api_model(name, broker, endpoints, msgs):
    context = {
        'name': name,
        'broker': broker,
        'endpoints': endpoints,
        'msgs': msgs
    }
    modelf = api_tpl.render(context)
    return modelf


def resource_to_endpoint(resource):
    iface = resource.interface
    msg = iface.msg
    etype = ''
    if iface.__class__.__name__ == 'AsyncConsumer':
        etype = 'subscriber'
    elif iface.__class__.__name__ == 'AsyncProducer':
        etype = 'publisher'
    elif iface.__class__.__name__ == 'ReqRespService':
        etype = 'rpc'
    elif iface.__class__.__name__ == 'ActionService':
        etype = 'action'
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


def r2api_m2m(resources, broker=None, name='MyAPI') -> str:
    if broker is None:
        _broker = {
            'type': 'MQTT',
            'host': 'localhost',
            'port': 1883,
            'username': '',
            'password': '',
        }
    else:
        _broker = {
            'host': broker.host,
            'port': broker.port,
        }
        if broker.__class__.__name__ == 'MQTTBroker':
            _broker['type'] = 'MQTT'
        elif broker.__class__.__name__ == 'RedisBroker':
            _broker['type'] = 'Redis'
        elif broker.__class__.__name__ == 'AMQPBroker':
            _broker['type'] = 'AMQP'
        if broker.auth is not None:
            if broker.auth.__class__.__name__ == 'BrokerAuthPlain':
                _broker['username'] = broker.auth.username
                _broker['password'] = broker.auth.password
    endpoints = []
    msgs = []
    for r in resources:
        e, msg = resource_to_endpoint(r)
        endpoints.append(e)
        msgs.append(msg)
    return build_api_model(name, _broker, endpoints, msgs)
