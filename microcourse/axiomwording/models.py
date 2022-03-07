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
from random import shuffle
import random

author = 'ML'

doc = """
Decisions
"""


class Constants(BaseConstants):
    name_in_url = 'axiomwording'
    players_per_group = None
    num_rounds = 8
    pairs1 = [[70, 70], [70, 70], [60, 60], [60, 60], [30, 30], [30, 30], [30, 20], [10, 20], [10, 10], [10, 10]]
    pairs2 = [[70, 10], [70, 10], [60, 70], [60, 70], [30, 60], [30, 60], [30, 30], [10, 30], [10, 20], [10, 20]]
    pairs3 = [[20, 60], [20, 60], [20, 60], [20, 60], [20, 60], [20, 60], [20, 60], [20, 60], [20, 60], [20, 20]]
    pairs4 = [[20, 60], [20, 60], [20, 60], [20, 60], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20]]
    pairs5 = [[60, 20], [60, 20], [60, 20], [20, 40], [20, 40], [20, 40], [20, 40], [20, 40], [20, 40], [20, 20]]
    pairs6 = [[60, 40], [60, 40], [60, 40], [20, 40], [20, 40], [20, 40], [20, 20], [20, 20], [20, 20], [20, 20]]
    pairs7 = [[50, 40], [50, 40], [50, 40], [50, 40], [50, 40], [50, 40], [10, 40], [10, 40], [10, 10], [10, 10]]
    pairs8 = [[50, 40], [50, 40], [50, 40], [50, 40], [50, 40], [50, 40], [10, 40], [10, 40], [40, 40], [40, 40]]
    all_pairs = [pairs1, pairs2, pairs3, pairs4, pairs5, pairs6, pairs7, pairs8]

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            order = []
            for x in range(10):
                order.append(x)
            shuffle(order)
            p.ord0 = order[0]
            p.ord1 = order[1]
            p.ord2 = order[2]
            p.ord3 = order[3]
            p.ord4 = order[4]
            p.ord5 = order[5]
            p.ord6 = order[6]
            p.ord7 = order[7]
            p.ord8 = order[8]
            p.ord9 = order[9]
            if self.round_number == 1:
                p.participant.vars['treatment'] = random.choice(['one', 'two'])
                p.participant.vars['distr_order'] = random.randint(0, 1)
                pairorder = []
                for x in range(8):
                    pairorder.append(x)
                shuffle(pairorder)
                p.participant.vars['pairorder1'] = pairorder[1]
                p.participant.vars['pairorder2'] = pairorder[2]
                p.participant.vars['pairorder3'] = pairorder[3]
                p.participant.vars['pairorder4'] = pairorder[4]
                p.participant.vars['pairorder5'] = pairorder[5]
                p.participant.vars['pairorder6'] = pairorder[6]
                p.participant.vars['pairorder7'] = pairorder[7]
                p.participant.vars['pairorder8'] = pairorder[0]
            p.pairord1 = p.participant.vars['pairorder1']
            p.pairord2 = p.participant.vars['pairorder2']
            p.pairord3 = p.participant.vars['pairorder3']
            p.pairord4 = p.participant.vars['pairorder4']
            p.pairord5 = p.participant.vars['pairorder5']
            p.pairord6 = p.participant.vars['pairorder6']
            p.pairord7 = p.participant.vars['pairorder7']
            p.pairord8 = p.participant.vars['pairorder8']
            p.treatment = p.participant.vars['treatment']
            p.distribution_order = p.participant.vars['distr_order']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()

    dec = models.IntegerField(
        label="Please choose:",
        choices=[
            [1, 'According to the rule, distribution A is preferable.'],
            [2, 'According to the rule, distribution B is preferable.'],
            [3, 'The rule is not applicable to find the preferable distribution out of these options.'],
        ],
        widget=widgets.RadioSelect
    )

    pairord1 = models.IntegerField()
    pairord2 = models.IntegerField()
    pairord3 = models.IntegerField()
    pairord4 = models.IntegerField()
    pairord5 = models.IntegerField()
    pairord6 = models.IntegerField()
    pairord7 = models.IntegerField()
    pairord8 = models.IntegerField()

    ord1 = models.IntegerField()
    ord2 = models.IntegerField()
    ord3 = models.IntegerField()
    ord4 = models.IntegerField()
    ord5 = models.IntegerField()
    ord6 = models.IntegerField()
    ord7 = models.IntegerField()
    ord8 = models.IntegerField()
    ord9 = models.IntegerField()
    ord0 = models.IntegerField()
    distribution_order = models.IntegerField()

    def set_payoffs(self) -> object:
        self.payoff = 0




