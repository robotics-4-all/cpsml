from .api import get_api_mm
from .communication import get_communication_mm
from .datatype import get_dtype_mm
from .networking import get_networking_mm
from .resource import get_resource_mm
from .thing import get_thing_mm
from .synthesis import get_synthesis_mm
from .eservice import get_eservice_mm
from .environment import get_env_mm
from .functionality import get_functionality_mm
from .entity import get_entity_mm
from .utils import build_model

from textx import (get_location, metamodel_from_str,
                   metamodel_for_language,
                   register_language, clear_language_registrations)
import textx.scoping.providers as scoping_providers
import textx.scoping as scoping
import textx.exceptions


def register_languages():
    clear_language_registrations()
    global_repo = scoping.GlobalModelRepository()
    global_repo_provider = scoping_providers.PlainNameGlobalRepo()
    thing_mm = get_thing_mm()
