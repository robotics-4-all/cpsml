from os.path import basename

from cpsml.lang import build_model
from cpsml.lang import get_resource_mm

from cpsml.transformations.thing2resources import thing_to_resources_m2m
from cpsml.transformations.resources2api import r2api_m2m


def thing_to_api_m2m(thing) -> str:
    resources_model_str = thing_to_resources_m2m(thing)
    rmm = get_resource_mm()
    rmodel = rmm.model_from_str(resources_model_str)
    api_model_str = r2api_m2m(rmodel.resources, thing.communication)
    return api_model_str
