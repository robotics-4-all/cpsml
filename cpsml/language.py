from textx import language

from cpsml.lang import (
    get_thing_mm,
    get_resource_mm,
    get_communication_mm,
    get_networking_mm,
    get_dtype_mm,
    get_api_mm,
    get_synthesis_mm
)


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


@language('cpsml-synth', '*.system')
def synthesis_language():
    "cpsml Synthesis language"
    mm = get_synthesis_mm()
    return mm
