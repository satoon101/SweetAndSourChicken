# ../sweet_and_sour_chicken/manager.py

"""Stores rewards/punishments and decides the choices."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from random import choice, randint


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'choice_manager',
)


# =============================================================================
# >> CLASSES
# =============================================================================
class _ChoiceManager(dict):
    rewards = dict()
    punishments = dict()

    def reward(self, name):
        if name in self.rewards:
            raise ValueError(
                'Reward "{name}" is already registered.'.format(
                    name=name,
                )
            )

        def inner(function):
            self.rewards[name] = function
        return inner

    def punishment(self, name):
        if name in self.punishments:
            raise ValueError(
                'Punishment "{name}" is already registered.'.format(
                    name=name,
                )
            )

        def inner(function):
            self.punishments[name] = function
        return inner

    def grant_choices(self, player):
        from .sweet_and_sour_chicken import (
            disabled_punishments, disabled_rewards, percent_for_both,
        )

        # Get the valid (not disabled) choices
        reward_choices = [
            y for x, y in self.rewards.items()
            if x not in disabled_rewards.get_string().split(',')
        ]
        punishment_choices = [
            y for x, y in self.punishments.items()
            if x not in disabled_punishments.get_string().split(',')
        ]

        # Are there no valid rewards nor valid punishments?
        if not reward_choices and not punishment_choices:
            raise ValueError('No valid rewards or punishments found.')

        # Are there no valid rewards?
        if not reward_choices and punishment_choices:
            choice(punishment_choices)(player)
            return

        # Are there no valid punishments?
        if not punishment_choices and reward_choices:
            choice(reward_choices)(player)
            return

        # Find if both a reward and a punishment should be chosen
        percent = min(max(percent_for_both.get_int(), 0), 100)
        both = False
        if percent:
            both = randint(1, 100) <= percent

        if both:
            choice(reward_choices)(player)
            choice(punishment_choices)(player)
            return

        if choice([0, 1]):
            choice(reward_choices)(player)
        else:
            choice(punishment_choices)(player)

choice_manager = _ChoiceManager()
