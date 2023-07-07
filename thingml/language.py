from textx import language

from thingml.utils import (
    get_thing_mm,
    get_resource_mm,
    get_networking_mm,
    get_communication_mm,
    get_dtype_mm
)


@language('thingml-thing', '*.thing')
def things_language():
    "thingml language"
    mm = get_thing_mm()
    return mm


@language('thingml-dtype', '*.dtype')
def dtypes_language():
    "thingml language for data types"
    mm = get_dtype_mm()
    return mm


@language('thingml-resource', '*.resource')
def resources_language():
    "thingml resource language"
    mm = get_resource_mm()
    return mm


@language('thingml-network', '*.net')
def networking_language():
    "thingml network language"
    mm = get_networking_mm()
    return mm


@language('thingml-comm', '*.comm')
def communication_language():
    "thingml communication language"
    mm = get_communication_mm()
    return mm
