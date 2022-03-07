from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class IntroPage(Page):

    def before_next_page(self):
        self.player.set_payoffs()


page_sequence = [IntroPage]
