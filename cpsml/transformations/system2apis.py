from os.path import basename

from cpsml.lang import build_model
from cpsml.lang import get_resource_mm

from cpsml.transformations.thing2resources import thing_to_resources_m2m
from cpsml.transformations.resources2api import resources_to_api_m2m


def system_to_apis_m2m(system) -> str:
    resources_model_str = thing_to_resources_m2m(thing)
    rmm = get_resource_mm()
    rmodel = rmm.model_from_str(resources_model_str)
    api_name = f'{thing.name}API'
    api_model_str = resources_to_api_m2m(rmodel.resources, thing.communication, api_name)
    return api_model_str
