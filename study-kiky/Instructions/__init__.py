
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    consent = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], initial=True, label='I consent to participate in this study. ')
    compre_mgr = models.IntegerField(choices=[[40, '40'], [30, '30'], [20, '20'], [10, '10'], [0, '0']], label="Firm's payoff")
    compre_mgr2 = models.IntegerField(choices=[[40, '40'], [30, '30'], [20, '20'], [10, '10'], [0, '0']], label="Firm's payoff")
    compre_ofc = models.IntegerField(choices=[[40, '40'], [30, '30'], [20, '20'], [10, '10'], [0, '0']], label="Official's payoff")
    compre_soc = models.IntegerField(choices=[[40, '40'], [30, '30'], [20, '20'], [10, '10'], [0, '0']], label="HIU's payoff")
    compre_soc2 = models.IntegerField(choices=[[40, '40'], [30, '30'], [20, '20'], [10, '10'], [0, '0']], label="HIU's payoff")
    time_outs = models.IntegerField(initial=0)
    firm_1 = models.IntegerField(label='Percentage of participants in the role of FIRMS who believe it is CORRECT to offer the transfer', max=100, min=0)
    firm_2 = models.IntegerField(label='Percentage of participants in the role of FIRMS who believe it is INCORRECT to offer the transfer', max=100, min=0)
    ofc_1 = models.IntegerField(label='Percentage of participants in the role of OFFICIALS who believe it is CORRECT to ACCEPT the transfer', max=100, min=0)
    ofc_2 = models.IntegerField(label='Percentage of participants in the role of OFFICIALS who believe it is INCORRECT to ACCEPT the transfer', max=100, min=0)
    num_failed = models.IntegerField(initial=0)
class InformationForm(Page):
    form_model = 'player'
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.consent=False
    @staticmethod
    def error_message(player: Player, values):
        solution = dict(
          consent=True
                  )
        error_messages = dict()
        for field_name in solution:
                if values [field_name] != solution[field_name]:
                    error_messages[field_name] = 'You cannot proceed to the next page without giving your consent. Please exit this webpage if you do not want to participate.'
        return error_messages
class GeneralInstruction(Page):
    form_model = 'player'
class Comprehension(Page):
    form_model = 'player'
    form_fields = ['compre_mgr', 'compre_ofc', 'compre_soc', 'compre_soc2', 'compre_mgr2']
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
           compre_mgr=40,
            compre_mgr2=20,
            compre_ofc=30,
            compre_soc=30,
            compre_soc2=0
                          )
        error_messages = dict()
        for field_name in solutions:
                if values [field_name] != solutions[field_name]:
                    player.num_failed += 1
                    error_messages[field_name] = 'Wrong answer'
        return error_messages
class NormElicitation(Page):
    form_model = 'player'
    form_fields = ['firm_1', 'firm_2', 'ofc_1', 'ofc_2']
    @staticmethod
    def error_message(player: Player, values):
        print ('values is', values)
        error_messages =""
        if values ['firm_1'] + values ['firm_2'] != 100 or values ['ofc_1'] + values['ofc_2'] !=100:
            error_messages = 'The total percentage must sum to 100.'
            return error_messages
page_sequence = [InformationForm, Consent, GeneralInstruction, Comprehension, NormElicitation]