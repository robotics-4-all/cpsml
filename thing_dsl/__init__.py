from textx import language

from thing_dsl.utils import get_mm

__version__ = "0.1.0.dev"


@language('thing_dsl', '*.thing')
def thing_dsl_language():
    "thing_dsl language"
    mm = get_mm()
    return mm
