# ../sweet_and_sour_chicken/punishments/__init__.py

"""All available punishments."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from warnings import warn

# Source.Python
from messages import SayText2
from paths import TRANSLATION_PATH
from translations.strings import LangStrings

# Plugin
from ..info import info


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'punishment_messages',
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
punishment_messages = {}

_punishment_path = TRANSLATION_PATH / info.name / 'punishments'
for _ini_file in _punishment_path.files('*.ini'):
    if _ini_file.stem.endswith('_server'):
        continue
    _instance = LangStrings(_ini_file.replace(TRANSLATION_PATH, '')[1:~3])
    for _key, _value in _instance.items():
        if _key in punishment_messages:
            warn(f'Translation key "{_key}" is already registered.')
            continue
        punishment_messages[_key] = SayText2(_value)
