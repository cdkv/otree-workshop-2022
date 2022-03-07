
from otree.api import *
c = cu

doc = 'The bribery game with separation between high and low corrupt players.'
class C(BaseConstants):
    NAME_IN_URL = 'main_stage'
    PLAYERS_PER_GROUP = None
    REAL_PLAYERS_PER_GROUP = 6
    NUM_ROUNDS = 4
    FIRM_ROLE = 'firm'
    OFFICIAL_ROLE = 'official'
    BRIBES_CUTOFF = 1
    OFFICIAL_CONDITIONS = ('honest', 'corrupt')
    FIRM_CONDITIONS = ('honest', 'corrupt')
    OFFICIAL_PAYOFF = (cu(30), cu(40))
    FIRM_PAYOFF = (cu(20), cu(30), cu(40))
    SOCIETY_PAYOFF = (cu(30), cu(0))
    TIME_OUT = 45
    TIME_OUT_FAST = 7
    MAX_TIME_OUTS = 2
class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    import random
    players = subsession.get_players()
    if subsession.round_number == 1:
        order_firm_condition = random.choices([True, False], k = len(players))
        order_official_condition = random.choices([True, False], k = len(players))
        for player in players:
            idx = player.id_in_subsession
            participant = player.participant
            participant.order_firm_condition = order_firm_condition[idx - 1]
            participant.order_official_condition = order_official_condition[idx - 1]
    
    for player in players:
        participant = player.participant
        player.firm_condition = C.FIRM_CONDITIONS[0] if (participant.order_firm_condition == (subsession.round_number in [1, 2])) else C.FIRM_CONDITIONS[1]
        player.official_condition = C.OFFICIAL_CONDITIONS[0] if (participant.order_official_condition == (subsession.round_number in [1, 3])) else C.OFFICIAL_CONDITIONS[1]
def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    import random
    if len(waiting_players) >= C.REAL_PLAYERS_PER_GROUP:
        minimum_per_role =  C.REAL_PLAYERS_PER_GROUP // 2
        firms = [p for p in waiting_players if p.participant.role == C.FIRM_ROLE]
        officials = [p for p in waiting_players if p.participant.role == C.OFFICIAL_ROLE]
        if len(firms) >= minimum_per_role and len(officials) >= minimum_per_role:
            new_firms = random.sample(firms, minimum_per_role)
            new_officials = random.sample(officials, minimum_per_role)
            return new_firms + new_officials
    
class Group(BaseGroup):
    pass
def get_decisions(group: Group):
    ### The idea of this function is to gather all decisions that are 
    ### relevant for a certain condition for the other role.
    players  = group.get_players()
    decisions = {}
    conditions = [(firm, official) for firm in C.FIRM_CONDITIONS for official in C.OFFICIAL_CONDITIONS]
    for c in conditions:
        decisions[c] = {C.FIRM_ROLE: [], C.OFFICIAL_ROLE: []}
    # gather all relevant decisions
    for p in players:
        all_rounds = p.in_all_rounds()
        role = p.participant.role
        corruption_type = "corrupt" if p.participant.bribes > C.BRIBES_CUTOFF else "honest" 
        if role == C.FIRM_ROLE:
            relevant_conditions = [(corruption_type, official) for official in C.OFFICIAL_CONDITIONS]
        elif role == C.OFFICIAL_ROLE:
            relevant_conditions = [(firm, corruption_type) for firm in C.FIRM_CONDITIONS]
        else:
            print("ohoh! Something is wrong with get_decisions")
        for rc in relevant_conditions:
            d = [r.decision for r in all_rounds if (r.firm_condition, r.official_condition) == rc]
            decisions[rc][role].extend(d)
    # add dummies if no real participants
    for cond in decisions:
        if len(decisions[cond][C.FIRM_ROLE]) == 0:
            decisions[cond][C.FIRM_ROLE] = [False, False, False, True] if cond[0] == 'honest' else [True, True, True, False]
        if len(decisions[cond][C.OFFICIAL_ROLE]) == 0:
            decisions[cond][C.OFFICIAL_ROLE] = [False, False, False, True] if cond[1] == 'honest' else [True, True, True, False]
    return(decisions)
def assign_decisions(group: Group):
    import random
    if group.round_number == C.NUM_ROUNDS:
        decisions = get_decisions(group)
        players = group.get_players()
        for p in players:
            role = p.participant.role
            other = C.FIRM_ROLE if role == C.OFFICIAL_ROLE else C.OFFICIAL_ROLE
            payment_round = random.choice(range(1, C.NUM_ROUNDS + 1))
            for r in p.in_all_rounds():
                r.other_decision = random.choice(decisions[(r.firm_condition, r.official_condition)][other])
                bribe = r.other_decision and r.decision
                r.payoff_society = C.SOCIETY_PAYOFF[bribe]
                if role == C.FIRM_ROLE:
                    firm_result = 1 + r.decision * (-1 + r.other_decision * 2)
                    r.payoff = C.FIRM_PAYOFF[firm_result]
                elif role == C.OFFICIAL_ROLE:
                    r.payoff = C.OFFICIAL_PAYOFF[bribe]
            p.participant.payment = random.choices([float(p.participant.payment), 
                                                    float(p.in_round(payment_round).payoff)], 
                                                   weights = [5, C.NUM_ROUNDS])
            p.participant.payoff = cu(p.participant.payment[0])
class Player(BasePlayer):
    decision = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']])
    other_decision = models.BooleanField()
    firm_condition = models.StringField()
    official_condition = models.StringField()
    payoff_society = models.CurrencyField(initial=30)
    time_outs = models.IntegerField(initial=0)
def calculating_time_out(player: Player):
    participant = player.participant
    if ( participant.time_outs > C.MAX_TIME_OUTS ):
        return C.TIME_OUT_FAST
    else:
        return C.TIME_OUT
def custom_export(players):
    yield ['participant_code', 'id_in_group', 'payment', 'bribes']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group, pp.payment, pp.bribes]
class WaitPageGrouping(WaitPage):
    group_by_arrival_time = True
    title_text = 'Please wait...'
    body_text = 'You will be associated with real people in this study. You are now waiting for the other participants to reach this stage. '
class InfoRoleFirm(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == C.FIRM_ROLE
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            participant.time_outs += 1
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class InfoRoleOfficial(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == C.OFFICIAL_ROLE
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            participant.time_outs += 1
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class FirmChoice(Page):
    form_model = 'player'
    form_fields = ['decision']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.participant.role == C.FIRM_ROLE
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import random
        if timeout_happened:
            player.time_outs += 1
            participant.time_outs += 1
            choices = [True, False, False, False] if participant.bribes < 3 else [True, True, True, False]
            player.decision = random.choice(choices)
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class OfficialChoice(Page):
    form_model = 'player'
    form_fields = ['decision']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.participant.role == C.OFFICIAL_ROLE
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import random
        if timeout_happened:
            player.time_outs += 1
            participant.time_outs += 1
            choices = [True, False, False, False] if participant.bribes < 3 else [True, True, True, False]
            player.decision = random.choice(choices)
        else: 
            participant.time_outs = 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
class EndOfDecisions(WaitPage):
    after_all_players_arrive = assign_decisions
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
class Feedback(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.finished = True
    @staticmethod
    def get_timeout_seconds(player: Player):
        return calculating_time_out(player)
page_sequence = [WaitPageGrouping, InfoRoleFirm, InfoRoleOfficial, FirmChoice, OfficialChoice, EndOfDecisions, Feedback]