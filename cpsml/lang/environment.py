from os.path import dirname, join, basename

from cpsml.utils import MODEL_REPO_PATH, THIS_DIR

from textx import metamodel_from_file, get_children_of_type
import textx.scoping.providers as scoping_providers


def get_env_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','environment.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "*.obstacles": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'environment','*.env')
            ),
            "*.things": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'things','*.thing')
            ),
        }
    )
    return mm
