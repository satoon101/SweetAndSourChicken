# ../sweet_and_sour_chicken/rewards/base.py

"""Base rewards."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Plugin
from . import reward_messages
from ..manager import choice_manager


# =============================================================================
# >> FUNCTIONS
# =============================================================================
@choice_manager.reward('speed_boost', reward_messages['speed_boost'])
def _speed_boost_player(player):
    player.speed *= 2


@choice_manager.reward('health', reward_messages['health'])
def _add_health(player):
    player.health += 50


@choice_manager.reward('armor', reward_messages['armor'])
def _add_armor(player):
    player.armor += 50
