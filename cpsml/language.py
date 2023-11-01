from textx import language

from cpsml.lang import (
    get_thing_mm,
    get_resource_mm,
    get_communication_mm,
    get_networking_mm,
    get_dtype_mm,
    get_api_mm,
    get_synthesis_mm,
    get_eservice_mm,
    get_env_mm,
    get_functionality_mm
)


@language('cpsml-thing', '*.thing')
def things_language():
    "CPS-ML Things language"
    mm = get_thing_mm()
    return mm


@language('cpsml-dtype', '*.dtype')
def dtypes_language():
    "CPS-ML DataType language"
    mm = get_dtype_mm()
    return mm


@language('cpsml-resource', '*.resource')
def resources_language():
    "CPS-ML Resource language"
    mm = get_resource_mm()
    return mm


@language('cpsml-network', '*.net')
def networking_language():
    "CPS-ML Networking language"
    mm = get_networking_mm()
    return mm


@language('cpsml-comm', '*.comm')
def communication_language():
    "CPS-ML Communication language"
    mm = get_communication_mm()
    return mm


@language('cpsml-api', '*.api')
def api_language():
    "CPS-ML API language"
    mm = get_api_mm()
    return mm


@language('cpsml-synth', '*.system')
def synthesis_language():
    "CPS-ML System Synthesis language"
    mm = get_synthesis_mm()
    return mm


@language('cpsml-esvc', '*.esvc')
def eservice_language():
    "CPS-ML Services language"
    mm = get_eservice_mm()
    return mm


@language('cpsml-env', '*.env')
def environment_language():
    "CPS-ML Environment language"
    mm = get_env_mm()
    return mm


@language('cpsml-func', '*.dfunc')
def functionality_language():
    "CPS-ML Functionality language"
    mm = get_functionality_mm()
    return mm
