# ../sweet_and_sour_chicken/rewards/__init__.py

"""All available rewards."""

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
    'reward_messages',
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
reward_messages = {}

_reward_path = TRANSLATION_PATH / info.name / 'rewards'
for _ini_file in _reward_path.files('*.ini'):
    if _ini_file.namebase.endswith('_server'):
        continue
    _instance = LangStrings(_ini_file.replace(TRANSLATION_PATH, '')[1:~3])
    for _key, _value in _instance.items():
        if _key in reward_messages:
            warn(
                'Translation key "{key}" is already registered.'.format(
                    key=_key,
                )
            )
            continue
        reward_messages[_key] = SayText2(_value)
