# ../sweet_and_sour_chicken/sweet_and_sour_chicken.py

"""Plugin that rewards/punishes players who kill chickens."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from importlib import import_module

# Site-package
from path import Path

# Source.Python
from config.manager import ConfigManager
from entities.entity import Entity
from events import Event
from listeners import OnLevelInit
from players.entity import Player
from translations.strings import LangStrings

# Plugin
from .info import info
from .manager import choice_manager


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'disabled_punishments',
    'disabled_rewards',
    'percent_for_both',
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_config_strings = LangStrings(info.name)
_base_path = Path(__file__).parent


# =============================================================================
# >> REGISTRATION
# =============================================================================
for _type in ('punishments', 'rewards'):
    for _file in _base_path.joinpath(_type).files('*.py'):
        if _file.namebase == '__init__':
            continue
        import_module(
            _file.replace(
                _base_path.parent,
                ''
            )[1:-3].replace('/', '.').replace('\\', '.')
        )


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with ConfigManager(info.name, 'sasc_') as _config:

    percent_for_both = _config.cvar(
        'percent_for_both', 50, _config_strings['percent_for_both']
    )

    disabled_punishments = _config.cvar(
        'disabled_punishments', '', _config_strings['disabled_punishments']
    )
    disabled_punishments.text(_config_strings['disabled_options'])
    disabled_punishments.text(
        '    ' + ','.join(choice_manager.punishments.keys())
    )

    disabled_rewards = _config.cvar(
        'disabled_rewards', '', _config_strings['disabled_rewards']
    )
    disabled_rewards.text(_config_strings['disabled_options'])
    disabled_rewards.text(
        '    ' + ','.join(choice_manager.rewards.keys())
    )

    chicken_count = _config.cvar(
        'chicken_count', 20, _config_strings['chicken_count']
    )


# =============================================================================
# >> LOAD & UNLOAD
# =============================================================================
@OnLevelInit
def load(map_name=None):
    map_info = Entity.find_or_create('info_map_parameters')
    map_info.pet_population = chicken_count.get_int()


# =============================================================================
# >> GAME EVENTS
# =============================================================================
@Event('other_death')
def _chicken_death(game_event):
    if game_event['othertype'] != 'chicken':
        return

    player = Player.from_userid(game_event['attacker'])
    choice_manager.grant_choices(player)
