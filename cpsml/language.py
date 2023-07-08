from textx import language

from cpsml.lang.thing import get_thing_mm
from cpsml.lang.resource import get_resource_mm
from cpsml.lang.communication import get_communication_mm
from cpsml.lang.networking import get_networking_mm
from cpsml.lang.datatype import get_dtype_mm
from cpsml.lang.api import get_api_mm


@language('cpsml-thing', '*.thing')
def things_language():
    "cpsml language"
    mm = get_thing_mm()
    return mm


@language('cpsml-dtype', '*.dtype')
def dtypes_language():
    "cpsml language for data types"
    mm = get_dtype_mm()
    return mm


@language('cpsml-resource', '*.resource')
def resources_language():
    "cpsml resource language"
    mm = get_resource_mm()
    return mm


@language('cpsml-network', '*.net')
def networking_language():
    "cpsml network language"
    mm = get_networking_mm()
    return mm


@language('cpsml-comm', '*.comm')
def communication_language():
    "cpsml communication language"
    mm = get_communication_mm()
    return mm


@language('cpsml-api', '*.api')
def api_language():
    "cpsml API language"
    mm = get_api_mm()
    return mm
