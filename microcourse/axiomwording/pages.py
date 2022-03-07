from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['dec']

    def vars_for_template(self):
        test=1
        data=[]
        if self.round_number == 1:
            pair = self.player.pairord1
        if self.round_number == 2:
            pair = self.player.pairord2
        if self.round_number == 3:
            pair = self.player.pairord3
        if self.round_number == 4:
            pair = self.player.pairord4
        if self.round_number == 5:
            pair = self.player.pairord5
        if self.round_number == 6:
            pair = self.player.pairord6
        if self.round_number == 7:
            pair = self.player.pairord7
        if self.round_number == 8:
            pair = self.player.pairord8
        data.append(Constants.all_pairs[pair][self.player.ord0])
        data.append(Constants.all_pairs[pair][self.player.ord1])
        data.append(Constants.all_pairs[pair][self.player.ord2])
        data.append(Constants.all_pairs[pair][self.player.ord3])
        data.append(Constants.all_pairs[pair][self.player.ord4])
        data.append(Constants.all_pairs[pair][self.player.ord5])
        data.append(Constants.all_pairs[pair][self.player.ord6])
        data.append(Constants.all_pairs[pair][self.player.ord7])
        data.append(Constants.all_pairs[pair][self.player.ord8])
        data.append(Constants.all_pairs[pair][self.player.ord9])

        data_a = []
        data_b = []

        if self.player.distribution_order == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.distribution_order == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])

        return dict(
            data_a=data_a,
            data_b=data_b,
            test=test,
        )

    def before_next_page(self):
        self.player.set_payoffs()


page_sequence = [DecisionPage]
