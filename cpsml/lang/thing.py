from os.path import dirname, join, basename

from cpsml.utils import MODEL_REPO_PATH, THIS_DIR

from textx import metamodel_from_file
import textx.scoping.providers as scoping_providers
from textx import (
    get_children_of_type,
)


def get_thing_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','thing.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "*.dataModel": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'datatypes','*.dtype')
            ),
            "*.sensors": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'things','*.thing')
            ),
            "*.actuators": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'things','*.thing')
            ),
            "*.networking": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'networks','*.net')
            ),
            "*.communication": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'communication','*.comm')
            )
        }
    )
    return mm
