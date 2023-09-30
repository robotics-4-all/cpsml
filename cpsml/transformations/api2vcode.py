from os.path import basename

from cpsml.lang import build_model
from cpsml.lang import get_resource_mm, get_api_mm


def api_to_vcode(thing_model, api_model) -> str:
    meta = api_model.metadata
    api = api_model.api
    return

