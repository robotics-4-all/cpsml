from os.path import dirname, join, basename
from textx import metamodel_from_file
import textx.scoping.providers as scoping_providers

from .mm_classes.datatype import type_builtins, PrimitiveDataType

THIS_DIR = dirname(__file__)
MODEL_REPO_PATH = join(THIS_DIR, '..', 'models')


def get_dtype_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','datatype.tx'),
        global_repository=True,
        classes=[PrimitiveDataType],
        builtins=type_builtins,
        debug=debug
    )
    return mm


def get_resource_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','resource.tx'),
        global_repository=True,
        classes=[PrimitiveDataType],
        builtins=type_builtins,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "types": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.dtype')
            ),
        }
    )
    return mm


def get_networking_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','networking.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "networks": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'networks','*.net')
            )
        }
    )
    return mm


def get_communication_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','communication.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "communication": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'communication','*.comm')
            )
        }
    )
    return mm


def get_api_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','api.tx'),
        global_repository=True,
        classes=[PrimitiveDataType],
        builtins=type_builtins,
        debug=debug
    )

    mm.register_scope_providers(
        {
            "types": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.dtype')
            ),
        }
    )
    return mm


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
    else:
        raise ValueError('Not a valid model extension.')
    model = mm.model_from_file(model_fpath)
    return model


def get_grammar(debug=False):
    with open(join(this_dir, 'cpsml.tx')) as f:
        return f.read()
