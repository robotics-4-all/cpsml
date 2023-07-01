from os.path import dirname, join, basename
from textx import metamodel_from_file
import textx.scoping.providers as scoping_providers

THIS_DIR = dirname(__file__)
MODEL_REPO_PATH = join(THIS_DIR, '..', 'models')


def get_thing_mm(debug=False):
    mm= metamodel_from_file(
        join(THIS_DIR, 'grammar','thing.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "*.dataModel": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.idl')
            ),
            "*.things": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'things','*.thing')
            ),
            "*.networks": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'networks','*.net')
            )
        }
    )
    return mm


def get_resource_mm(debug=False):
    mm= metamodel_from_file(
        join(THIS_DIR, 'grammar','resource.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "*.inDataType": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.idl')
            ),
            "*.outDataType": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.idl')
            )
        }
    )
    return mm


def get_networking_mm(debug=False):
    mm= metamodel_from_file(
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


def get_comm_language(debug=False):
    mm= metamodel_from_file(
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


def build_model(model_fpath):
    model_filename = basename(model_fpath)
    if model_filename.endswith('.net'):
        mm = get_networking_mm()
    elif model_filename.endswith('.thing'):
        mm = get_thing_mm()
    elif model_filename.endswith('.resource'):
        mm = get_resource_mm()
    else:
        raise ValueError('Not a valid model extension.')
    model = mm.model_from_file(model_fpath)
    return model


def get_grammar(debug=False):
    with open(join(this_dir, 'thingml.tx')) as f:
        return f.read()
