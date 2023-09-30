from typing import Dict, Any, List

from cpsml.lang import build_model
from cpsml.lang import get_eservice_mm

from openapi_parser import parse
from pydantic import BaseModel

from cpsml.utils import TEMPLATES_PATH

import jinja2

# Initialize template engine.
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    trim_blocks=True,
    lstrip_blocks=True
)

eservice_tpl = jinja_env.get_template('eservice.jinja')



class Param(BaseModel):
    name: str
    type: str


class EServiceParams(BaseModel):
    body: List[Param] = []
    query: List[Param] = []
    path: List[Param] = []


class EService(BaseModel):
    name: str
    host: str
    port: int
    ssl: bool
    path: str
    verb: str
    params: EServiceParams


def parse_openapi3_spec_file(filepath: str) -> List:
    esvcs = []
    content = parse(filepath)
    server = content.servers[0]
    schema, host, port = server.url.split(':')
    host = host[2:]
    paths = content.paths
    for path in paths:
        for op in path.operations:
            name = op.operation_id or path.url.remove('/') + op.method
            ssl = True if schema == 'https' else False
            qparams = []
            pparams = []
            bparams = []
            if op.request_body:
                for param in op.request_body.content:
                    for p in param.schema.properties:
                        bparams.append(Param(
                            name=p.name,
                            type=p.schema.type.name
                        ))
            for param in op.parameters:
                if param.location.name == 'QUERY':
                    qparams.append(Param(
                        name=param.name,
                        type=param.schema.type.name
                    ))
                if param.location.name == 'PATH':
                    pparams.append(Param(
                        name=param.name,
                        type=param.schema.type.name
                    ))
            esvc = EService(
                name=name,
                host=host,
                port=int(port),
                ssl=ssl,
                path=path.url,
                verb=op.method.name,
                params=EServiceParams(
                    body=bparams,
                    query=qparams,
                    path=pparams,
                )
            )
            esvcs.append(esvc)
    return esvcs


def build_eservice_model(eservices):
    context = {
        'eservices': eservices
    }
    modelf = eservice_tpl.render(context)
    return modelf



def openapi_2_eservices_mm(filepath: str):
    eservices = parse_openapi3_spec_file(filepath)
    model = build_eservice_model(eservices)
    return model
