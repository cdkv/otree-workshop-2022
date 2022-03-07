from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'ML'

doc = """
Axiom stage
"""


class Constants(BaseConstants):
    name_in_url = 'sca'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    axiom_rawls = models.IntegerField(
        label="Please choose your commitment to the principle:",
        choices=[
            [1, 'I want to commit to the principle.'],
            [0, 'I do not want to commit, but decide case by case.'],
        ],
        widget = widgets.RadioSelect
)

    def set_payoffs(self) -> object:
        self.payoff = 0
