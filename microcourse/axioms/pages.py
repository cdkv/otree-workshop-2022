from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionPage(Page):
    pass

class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['axiom_rawls']

    def before_next_page(self):
        self.player.set_payoffs()


page_sequence = [InstructionPage, DecisionPage]
