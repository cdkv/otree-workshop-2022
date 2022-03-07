from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class CharityGiving(Page):
    form_model = 'player'
    form_fields = ['donation']

    def error_message(self, values):
        if not values['donation']:
            return 'Please decide how much you want to donate to charity. If you do not want to donate any of your ' \
                   'ECUs, you can set the slider to zero.'

    def before_next_page(self):
        self.player.set_payoffs()


class ControlQuestions(Page):
    form_model = 'player'
    form_fields = ['income', 'justworld', 'political_right', 'check_political_right', 'check_justworld']

page_sequence = [CharityGiving, ControlQuestions]
