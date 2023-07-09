from os.path import dirname, join, basename

from cpsml.utils import MODEL_REPO_PATH, THIS_DIR

from textx import metamodel_from_file
import textx.scoping.providers as scoping_providers
from textx import (
    get_children_of_type,
)


def get_synthesis_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','synthesis.tx'),
        global_repository=True,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "*.things": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'things','*.thing')
            ),
            "*.communication": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'communication','*.comm')
            ),
            "*.services": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'eservices','*.esvc')
            ),
        }
    )
    return mm

