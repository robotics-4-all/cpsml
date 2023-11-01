from os.path import dirname, join, basename
from textx import metamodel_from_file
import textx.scoping.providers as scoping_providers

from cpsml.utils import MODEL_REPO_PATH

from cpsml.lang import (
    get_thing_mm,
    get_resource_mm,
    get_communication_mm,
    get_networking_mm,
    get_dtype_mm,
    get_api_mm,
    get_synthesis_mm,
    get_eservice_mm,
    get_env_mm,
    get_functionality_mm
)


def build_model(model_fpath):
    model_filename = basename(model_fpath)
    if model_filename.endswith('.net'):
        mm = get_networking_mm()
    elif model_filename.endswith('.thing'):
        mm = get_thing_mm()
    elif model_filename.endswith('.resource'):
        mm = get_resource_mm()
    elif model_filename.endswith('.comm'):
        mm = get_communication_mm()
    elif model_filename.endswith('.dtype'):
        mm = get_dtype_mm()
    elif model_filename.endswith('.api'):
        mm = get_api_mm()
    elif model_filename.endswith('.system'):
        mm = get_synthesis_mm()
    elif model_filename.endswith('.esvc'):
        mm = get_eservice_mm()
    elif model_filename.endswith('.env'):
        mm = get_env_mm()
    elif model_filename.endswith('.dfunc'):
        mm = get_functionality_mm()
    else:
        raise ValueError('Not a valid model extension.')
    model = mm.model_from_file(model_fpath)
    return model
