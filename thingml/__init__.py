from textx import language

from thingml.utils import get_mm

__version__ = "0.1.0.dev"


@language('thingml', '*.thing')
def thingml_language():
    "thingml language"
    mm = get_mm()
    return mm
