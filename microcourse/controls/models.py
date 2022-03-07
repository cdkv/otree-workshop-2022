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
Controls
"""


class Constants(BaseConstants):
    name_in_url = 'c_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    political_right = models.IntegerField()
    check_political_right = models.IntegerField()
    income = models.IntegerField(
        choices=[[1, 'below 1,000'], [2, 'between 1,000 and 2,000'], [3, 'between 2,000 and 3,000'], [4, 'between 3,000 and 4,000'], [5, 'between 4,000 and 5,000'], [6, 'more than 5,000']],
        label='What is your (approximate) monthly gross income (in GBP)?'
    )
    justworld = models.IntegerField()
    check_justworld = models.IntegerField()
    donation = models.IntegerField(label="Please choose how many ECUs you would like to donate to charity.",
                                   min=0,
                                   max=1000)

    def set_payoffs(self) -> object:
        self.payoff = 0