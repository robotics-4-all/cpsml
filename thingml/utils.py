from os.path import dirname, join
from textx import metamodel_from_file
import textx.scoping.providers as scoping_providers

THIS_DIR = dirname(__file__)
MODEL_REPO_PATH = join(THIS_DIR, '..', 'models')

def get_thing_mm(debug=False):
    """
    """
    mm= metamodel_from_file(
        join(THIS_DIR, 'grammar','thing.tx'),
        global_repository=True,
        debug=debug
    )

    # mm.register_scope_providers(
    #     {
    #         "*.*": scoping_providers.FQNImportURI(
    #             importAs=True,
    #             # importURI_to_scope_name=importURI_to_scope_name
    #         )
    #     }
    # )
    mm.register_scope_providers(
        {
            "*.dataModel": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.idl')
            ),
            "*.things": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'things','*.thing')
            )
        }
    )

    return mm


def get_resource_mm(debug=False):
    """
    """
    mm= metamodel_from_file(
        join(THIS_DIR, 'grammar','resource.tx'),
        global_repository=True,
        debug=debug
    )

    # mm.register_scope_providers(
    #     {
    #         "*.*": scoping_providers.FQNImportURI(
    #             importAs=True,
    #             # importURI_to_scope_name=importURI_to_scope_name
    #         )
    #     }
    # )
    # mm.register_scope_providers(
    #     {
    #         "*.dataModel": scoping_providers.FQNGlobalRepo(
    #             join(MODEL_REPO_PATH, 'datatypes','*.idl')
    #         ),
    #         "*.things": scoping_providers.FQNGlobalRepo(
    #             join(MODEL_REPO_PATH, 'things','*.thing')
    #         )
    #     }
    # )

    return mm

def build_model(model_fpath):
    mm = get_mm(global_scope=True)
    model = mm.model_from_file(model_fpath)
    # print(model._tx_loaded_models)
    reg_models = mm._tx_model_repository.all_models.filename_to_model
    models = [val for key, val in reg_models.items() if val != model]
    return (model, models)


def get_grammar(debug=False):
    with open(join(this_dir, 'thingml.tx')) as f:
        return f.read()
