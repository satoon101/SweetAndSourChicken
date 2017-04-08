# ../sweet_and_sour_chicken/manager.py

"""Stores rewards/punishments and decides the choices."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from collections import namedtuple
from random import choice, randint


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'choice_manager',
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# pylint: disable=invalid-name
Choice = namedtuple(typename='Choice', field_names=('message', 'function'))


# =============================================================================
# >> CLASSES
# =============================================================================
class _ChoiceManager(object):
    """Class used to hold rewards/punishments."""

    rewards = dict()
    punishments = dict()

    def reward(self, name, message):
        """Decorator that registers the function as a reward."""
        if name in self.rewards:
            raise ValueError(
                'Reward "{name}" is already registered.'.format(
                    name=name,
                )
            )

        def inner(function):
            """Register the reward function."""
            self.rewards[name] = Choice(message=message, function=function)
        return inner

    def punishment(self, name, message):
        """Decorator that registers the function as a punishment."""
        if name in self.punishments:
            raise ValueError(
                'Punishment "{name}" is already registered.'.format(
                    name=name,
                )
            )

        def inner(function):
            """Register the punishment function."""
            self.punishments[name] = Choice(message=message, function=function)
        return inner

    def grant_choices(self, player):
        """Grant the random choices for reward/punishment."""
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
            self.enact_choices_for_player(
                choices=[choice(punishment_choices)],
                player=player,
            )
            return

        # Are there no valid punishments?
        if not punishment_choices and reward_choices:
            self.enact_choices_for_player(
                choices=[choice(reward_choices)],
                player=player,
            )
            return

        # Find if both a reward and a punishment should be chosen
        percent = min(max(percent_for_both.get_int(), 0), 100)
        both = False
        if percent:
            both = randint(1, 100) <= percent

        if both:
            choices = [choice(reward_choices), choice(punishment_choices)]
        elif choice([0, 1]):
            choices = [choice(reward_choices)]
        else:
            choices = [choice(punishment_choices)]

        self.enact_choices_for_player(
            choices=choices,
            player=player,
        )

    @staticmethod
    def enact_choices_for_player(choices, player):
        """Reward/punish player and send message."""
        for item in choices:
            item.function(player)
            item.message.send(player.index)

choice_manager = _ChoiceManager()
