from textx import language

from thingml.utils import get_thing_mm, get_resource_mm


@language('thingml-things', '*.thing')
def things_language():
    "thingml language"
    mm = get_thing_mm()
    return mm

@language('thingml-resources', '*.resource')
def resources_language():
    "thingml language"
    mm = get_resource_mm()
    return mm

