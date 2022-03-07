from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class InstructionPage(Page):
    def vars_for_template(self):
        url1 = "https://i.ibb.co/s3BsVT0/piechart-example.png"

        return dict(
            url1=url1,
        )

class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['dec1']

    def vars_for_template(self):
        url1 = "https://i.ibb.co/s3BsVT0/piechart-example.png"

        return dict(
            url1=url1,
        )

    def before_next_page(self):
        self.player.set_payoffs()


page_sequence = [InstructionPage, DecisionPage]
