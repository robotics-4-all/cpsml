from os.path import dirname, join, basename

from cpsml.utils import MODEL_REPO_PATH, THIS_DIR

from textx import metamodel_from_file, get_children_of_type
import textx.scoping.providers as scoping_providers


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
