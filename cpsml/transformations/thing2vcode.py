from os.path import basename
import jinja2

from cpsml.utils import TEMPLATES_PATH
from cpsml.lang import build_model
from cpsml.lang import get_resource_mm, get_api_mm

from cpsml.transformations.thing2resources import thing_to_resources_m2m
from cpsml.transformations.resources2api import resources_to_api_m2m


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    trim_blocks=True,
    lstrip_blocks=True
)

vthing_tpl = jinja_env.get_template('vthing.jinja')


def build_vthing(thing, api):
    context = {
        'thing': thing,
        'api': api,
    }
    modelf = vthing_tpl.render(context)
    return modelf


def thing_to_vcode(thing) -> str:
    resources_model_str = thing_to_resources_m2m(thing)
    rmm = get_resource_mm()
    rmodel = rmm.model_from_str(resources_model_str)
    api_name = f'{thing.name}API'
    api_model_str = resources_to_api_m2m(rmodel.resources, thing.communication, api_name)
    api_mm = get_api_mm()
    api_model = api_mm.model_from_str(api_model_str)

    meta = api_model.metadata
    api = api_model.api

    vthing_str = build_vthing(thing, api)
    print(vthing_str)
    return api_model_str
