# ../sweet_and_sour_chicken/punishments/base.py

"""Base punishments."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Plugin
from . import punishment_messages
from ..manager import choice_manager


# =============================================================================
# >> FUNCTIONS
# =============================================================================
@choice_manager.punishment('slow', punishment_messages['slow'])
def _slow_player(player):
    player.speed *= .5


@choice_manager.punishment('damage', punishment_messages['damage'])
def _damage_player(player):
    player.take_damage(50)


@choice_manager.punishment('kill', punishment_messages['kill'])
def _kill_player(player):
    player.slay()
