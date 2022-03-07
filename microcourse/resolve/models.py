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
resolve
"""


class Constants(BaseConstants):
    name_in_url = 'res'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    axiom_rawls_revised = models.IntegerField(
        label="Please choose your commitment to the principle:",
        choices=[
            [1, 'I want to commit to the principle.'],
            [0, 'I do not want to commit, but decide case by case.'],
        ],
        widget=widgets.RadioSelect
    )

    dec1_revised = models.IntegerField(
        label="Please choose which program should be implemented:",
        choices=[
            [1, 'I want program A to be implemented.'],
            [2, 'I want program B to be implemented.'],
        ],
        widget=widgets.RadioSelect
    )

    def set_payoffs(self) -> object:
        self.payoff = 0
