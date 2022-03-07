
from otree.api import *
c = cu

doc = 'The bribery game with random matching for multiple rounds'
class C(BaseConstants):
    NAME_IN_URL = 'initial_stage2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    PLAYERS_IN_SESSION = 6
    ENDOWMENT_FIRM = cu(30)
    ENDOWMENT_OFFICIAL = cu(30)
    ENDOWMENT_SOCIETY = cu(30)
    PRICE_OFFER = cu(10)
    ACCEPTANCE_PAYOFF = cu(20)
    SOCIETAL_COST = cu(30)
    FIRM_ROLE = 'firm'
    OFFICIAL_ROLE = 'official'
    TIME_OUT = 30
    TIME_OUT_FAST = 3
    MAX_TIME_OUTS = 1
    FIRM_CHOICE = ('offer', 'not offer')
    OFFICIAL_CHOICE = ('accept', 'reject')
class Subsession(BaseSubsession):
    average_offer = models.FloatField(initial=0.5)
    average_accept = models.FloatField(initial=0.5)
    assignment_time = models.FloatField(initial=2000000000)
def creating_session(subsession: Subsession):
    session = subsession.session
    # initialise the time_outs
    if subsession.round_number == 1:
        players = subsession.get_players()
        for p in players:
            p.participant.time_outs = 0
            p.participant.bribes = 0
    
    
    
    
def calculating_averages(subsession: Subsession):
    session = subsession.session
    import statistics
    if subsession.round_number == 1:
        subsession.average_offer = .5
        subsession.average_accept = .5
    else:
        prev_round = subsession.in_round(subsession.round_number - 1)
        groups = prev_round.get_groups()
        groups = [g for g in groups if g.field_maybe_none('firm_offer') is not None and g.field_maybe_none('official_accept') is not None]
        subsession.average_offer = statistics.mean([g.firm_offer for g in groups])
        subsession.average_accept = statistics.mean([g.official_accept for g in groups])
    
    
    
    
    
def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    session = subsession.session
    import random
    import time
    print("round", subsession.round_number)
    print("waiting:", len(waiting_players))
    print("diff:", time.time() - subsession.assignment_time)
    too_long = (time.time() - subsession.assignment_time) > 30
    if subsession.round_number == 1 and len(waiting_players) >= C.PLAYERS_PER_GROUP:
        new_players = random.sample(waiting_players, C.PLAYERS_PER_GROUP)
        return new_players
    elif subsession.round_number > 1 and (len(waiting_players) >= C.PLAYERS_IN_SESSION or too_long):
        firms = [p for p in waiting_players if p.role == C.FIRM_ROLE]
        officials = [p for p in waiting_players if p.role == C.OFFICIAL_ROLE]
        if min(len(firms), len(officials)) >= 1:
            subsession.assignment_time = time.time()
            new_players = [random.choice(firms), random.choice(officials)]
            return new_players
class Group(BaseGroup):
    firm_offer = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']])
    official_accept = models.BooleanField()
def calculate_round_payoffs(group: Group):
    import random
    p1 = group.get_player_by_role(C.FIRM_ROLE)
    p2 = group.get_player_by_role(C.OFFICIAL_ROLE)
    p1.payoff = C.ENDOWMENT_FIRM + group.firm_offer * ( - C.PRICE_OFFER + group.official_accept * C.ACCEPTANCE_PAYOFF)
    p2.payoff= C.ENDOWMENT_OFFICIAL + group.firm_offer * C.PRICE_OFFER * group.official_accept
    p1.payoff_society = C.ENDOWMENT_SOCIETY - group.firm_offer * group.official_accept * C.SOCIETAL_COST
    p2.payoff_society = p1.payoff_society
    
    p1.participant.bribes += group.firm_offer
    p2.participant.bribes += group.official_accept
    
    if group.round_number == C.NUM_ROUNDS:
        payoffs1 = [p.payoff for p in p1.in_all_rounds()]
        payoffs2 = [p.payoff for p in p2.in_all_rounds()]
        p1.participant.payment = float(random.choice(payoffs1))
        p2.participant.payment = float(random.choice(payoffs2))
class Player(BasePlayer):
    firm_choice = models.StringField(initial='0')
    official_choice = models.StringField(initial='0')
    payoff_society = models.CurrencyField(initial=C.ENDOWMENT_SOCIETY)
def calculating_time_out(player: Player):
    participant = player.participant
    if ( participant.time_outs > C.MAX_TIME_OUTS ):
        return C.TIME_OUT_FAST
    else:
        return C.TIME_OUT
def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]
class WaitPageForGrouping(WaitPage):
    group_by_arrival_time = True
    title_text = 'Please wait...'
    body_text = 'You will be associated with real people in this study. You are now waiting for the other participants to reach this stage. '
class AdditionalInfo(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class FirmChoice(Page):
    form_model = 'group'
    form_fields = ['firm_offer']
    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.FIRM_ROLE
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        subsession = player.subsession
        group = player.group
        participant = player.participant
        if timeout_happened:
            import random
            calculating_averages(subsession)
            participant.time_outs += 1
            group.firm_offer = ( random.random() < subsession.average_offer )
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class OfficialChoice(Page):
    form_model = 'group'
    form_fields = ['official_accept']
    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.OFFICIAL_ROLE
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        subsession = player.subsession
        group = player.group
        participant = player.participant
        if timeout_happened:
            import random
            calculating_averages(subsession)
            participant.time_outs += 1
            group.official_accept = ( random.random() < subsession.average_accept )
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class WaitForResponses(WaitPage):
    after_all_players_arrive = calculate_round_payoffs
class Feedback(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.role = player.role
        if timeout_happened:
            participant.time_outs += 1
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
page_sequence = [WaitPageForGrouping, AdditionalInfo, FirmChoice, OfficialChoice, WaitForResponses, Feedback]