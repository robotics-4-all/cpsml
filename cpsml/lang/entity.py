from os.path import dirname, join, basename

from textx import metamodel_from_file, get_children_of_type
import textx.scoping.providers as scoping_providers

from cpsml.utils import MODEL_REPO_PATH, THIS_DIR
from cpsml.mm_classes.datatype import type_builtins, PrimitiveDataType


def get_entity_mm(debug=False):
    mm = metamodel_from_file(
        join(THIS_DIR, 'grammar','entity.tx'),
        global_repository=True,
        classes=[PrimitiveDataType],
        builtins=type_builtins,
        debug=debug
    )
    mm.register_scope_providers(
        {
            "*.*": scoping_providers.FQNImportURI(),
            "*.entities": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'entities','*.ent')
            ),
            "*.communication": scoping_providers.FQNGlobalRepo(
                join(MODEL_REPO_PATH, 'communication','*.comm')
            ),
        }
    )
    return mm
