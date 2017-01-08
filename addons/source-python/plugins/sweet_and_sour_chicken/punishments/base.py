# ../sweet_and_sour_chicken/punishments/base.py

"""Base punishments."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Plugin
from ..manager import choice_manager


# =============================================================================
# >> FUNCTIONS
# =============================================================================
@choice_manager.punishment('slow')
def _slow_player(player):
    player.speed *= .5


@choice_manager.punishment('damage')
def _damage_player(player):
    player.take_damage(50)


@choice_manager.punishment('kill')
def _kill_player(player):
    player.slay()
