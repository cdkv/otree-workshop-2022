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
ASCMS_XP_Main
"""


class Constants(BaseConstants):
    name_in_url = 'xp_m'
    players_per_group = None
    num_rounds = 3

    #build core data: 5 axioms, 5 sets of 8 pairs of distributions of 10 incomes
    #order of axioms and distributions matter (1 to 5) - Rawls, Efficiency, Gini, Pigou-Dalton, Hammond
    #within each pair, the first is in favor of axiom and the second in favor of anti-axiom
    axioms1 = ["Program A is preferable compared to program B if the lowest income in program A is larger than the lowest income in program B.","Program A is preferable compared to program B if the lowest income in program A is smaller than the lowest income in program B."]
    axioms2 = ["Program A is preferable compared to program B if the sum of all incomes of program A is larger than the sum of all incomes of program B.", "Program A is preferable compared to program B if the sum of all incomes of program A is smaller than the sum of all incomes of program B."]
    axioms3 = ["Program A is preferable compared to program B if the expected income difference of two randomly chosen persons is smaller in program A than the expected income difference of two randomly chosen persons in program B.", "Program A is preferable compared to program B if the expected income difference of two randomly chosen persons is larger in program A than the expected income difference of two randomly chosen persons in program B."]
    axioms4 = ["Program A is preferable compared to program B if there is a way to re-allocate income starting from program B and yielding program A such that re-allocations only involve transfers from individuals with higher incomes to individuals with lower incomes.", "Program A is preferable compared to program B if there is a way to re-allocate income starting from program B and yielding program A such that re-allocations only involve transfers from individuals with lower incomes to individuals with higher incomes."]
    axioms5 = ["Program A is preferable compared to program B if there are two or more persons such that the poorest of them earns more in A than in B, and the total earnings in A are at most as much as in B. All other persons receive the same under both programs.", "Program A is preferable compared to program B if there are two or more persons such that the poorest of them earns less in A than in B, and the total earnings in A are at least as much as in B. All other persons receive the same under both programs."]
    all_axioms = [axioms1, axioms2, axioms3, axioms4, axioms5]

    pairs1_1 = [[7196, 5486], [1497, 5486], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212]]
    pairs2_1 = [[7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [2922, 6911], [2922, 1212]]
    pairs3_1 = [[7196, 6199], [7196, 6199], [7196, 6199], [7196, 6199], [2209, 6199], [2209, 6199], [2209, 1212], [2209, 1212], [2209, 1212], [2209, 1212]]
    pairs4_1 = [[7196, 5486], [7196, 5486], [7196, 5486], [2922, 5486], [2922, 5486], [2922, 5486], [2922, 5486], [2922, 1212], [2922, 1212], [2922, 1212]]
    pairs5_1 = [[2708, 7196], [2708, 7196], [2708, 7196], [2708, 7196], [2708, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212]]
    pairs6_1 = [[4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 1212], [2708, 1212], [2708, 1212], [2708, 1212], [2708, 1212], [2708, 1212]]
    pairs7_1 = [[7196, 3516], [7196, 3516], [7196, 3516], [1610, 3516], [1610, 3516], [1610, 3516], [1610, 3516], [1610, 3516], [1610, 3516], [1610, 1212]]
    pairs8_1 = [[1610, 7196], [1610, 7196], [1610, 7196], [1610, 7196], [1610, 7196], [1610, 7196], [1610, 7196], [1610, 7196], [1610, 7196], [1610, 1212]]
    pairs_1 = [pairs1_1, pairs2_1, pairs3_1, pairs4_1, pairs5_1, pairs6_1, pairs7_1, pairs8_1]
    pairs1_2 = [[7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [1212, 4204], [1212, 4204], [1212, 4204], [1212, 4204]]
    pairs2_2 = [[7196, 4204], [7196, 4204], [7196, 4204], [1212, 4204], [1212, 4204], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs3_2 = [[7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [1212, 4204], [1212, 4204], [1212, 4204], [1212, 1212]]
    pairs4_2 = [[7196, 4204], [7196, 4204], [1212, 4204], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs5_2 = [[7196, 2708], [7196, 2708], [7196, 2708], [7196, 2708], [1212, 2708], [1212, 4204], [1212, 4204], [1212, 4204], [1212, 4204], [1212, 4204]]
    pairs6_2 = [[7196, 4204], [7196, 4204], [7196, 4204], [7196, 4204], [1212, 4204], [1212, 2708], [1212, 2708], [1212, 2708], [1212, 2708], [1212, 2708]]
    pairs7_2 = [[7196, 5700], [7196, 5700], [7196, 5700], [7196, 5700], [7196, 5700], [1212, 5700], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs8_2 = [[7196, 5700], [7196, 5700], [7196, 5700], [7196, 5700], [7196, 5700], [1212, 5700], [5700, 5700], [5700, 5700], [5700, 5700], [5700, 5700]]
    pairs_2 = [pairs1_2, pairs2_2, pairs3_2, pairs4_2, pairs5_2, pairs6_2, pairs7_2, pairs8_2]
    pairs1_3 = [[7196, 5486], [1497, 5486], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212], [1497, 1212]]
    pairs2_3 = [[7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [7196, 6911], [2922, 6911], [2922, 1212]]
    pairs3_3 = [[7196, 5486], [7196, 5486], [7196, 5486], [2922, 5486], [2922, 5486], [2922, 5486], [2922, 5486], [2922, 1212], [2922, 1212], [2922, 1212]]
    pairs4_3 = [[1212, 1212], [1212, 7196], [1212, 7196], [1212, 7196], [1212, 7196], [1212, 7196], [1212, 7196], [1212, 7196], [1212, 7196], [1212, 7196]]
    pairs5_3 = [[5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 1212], [5700, 1212], [1212, 1212], [1212, 1212]]
    pairs6_3 = [[5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 1212], [5700, 1212], [5700, 5700], [5700, 5700]]
    pairs7_3 = [[7196, 7196], [7196, 7196], [6199, 6199], [6199, 6199], [3207, 3207], [3207, 3207], [2209, 3207], [2209, 1212], [1212, 1212], [1212, 1212]]
    pairs8_3 = [[1212, 7196], [1212, 7196], [7196, 6199], [7196, 6199], [6199, 3207], [6199, 3207], [3207, 3207], [3207, 1212], [2209, 1212], [2209, 1212]]
    pairs_3 = [pairs1_3, pairs2_3, pairs3_3, pairs4_3, pairs5_3, pairs6_3, pairs7_3, pairs8_3]
    pairs1_4 = [[7196, 7196], [7196, 7196], [6199, 6199], [6199, 6199], [3207, 3207], [3207, 3207], [2209, 3207], [2209, 1212], [1212, 1212], [1212, 1212]]
    pairs2_4 = [[1212, 7196], [1212, 7196], [7196, 6199], [7196, 6199], [6199, 3207], [6199, 3207], [3207, 3207], [3207, 1212], [2209, 1212], [2209, 1212]]
    pairs3_4 = [[5201, 7196], [5201, 7196], [5201, 7196], [5201, 7196], [5201, 7196], [5201, 7196], [5201, 1212], [5201, 1212], [5201, 1212], [1212, 1212]]
    pairs4_4 = [[5201, 7196], [5201, 7196], [5201, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs5_4 = [[1212, 7196], [1212, 7196], [1212, 7196], [1212, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212]]
    pairs6_4 = [[4204, 7196], [4204, 7196], [4204, 7196], [4204, 1212], [4204, 1212], [4204, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs7_4 = [[5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 1212], [5700, 1212], [1212, 1212], [1212, 1212]]
    pairs8_4 = [[5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 1212], [5700, 1212], [5700, 5700], [5700, 5700]]
    pairs_4 = [pairs1_4, pairs2_4, pairs3_4, pairs4_4, pairs5_4, pairs6_4, pairs7_4, pairs8_4]
    pairs1_5 = [[4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212]]
    pairs2_5 = [[4204, 7196], [4204, 7196], [4204, 7196], [4204, 1212], [4204, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs3_5 = [[4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 1212], [4204, 1212], [4204, 1212], [1212, 1212]]
    pairs4_5 = [[4204, 7196], [4204, 7196], [4204, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs5_5 = [[2708, 7196], [2708, 7196], [2708, 7196], [2708, 7196], [2708, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212], [4204, 1212]]
    pairs6_5 = [[4204, 7196], [4204, 7196], [4204, 7196], [4204, 7196], [4204, 1212], [2708, 1212], [2708, 1212], [2708, 1212], [2708, 1212], [2708, 1212]]
    pairs7_5 = [[5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 1212], [1212, 1212], [1212, 1212], [1212, 1212], [1212, 1212]]
    pairs8_5 = [[5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 7196], [5700, 1212], [5700, 5700], [5700, 5700], [5700, 5700], [5700, 5700]]
    pairs_5 = [pairs1_5, pairs2_5, pairs3_5, pairs4_5, pairs5_5, pairs6_5, pairs7_5, pairs8_5]
    all_pairs = [pairs_1, pairs_2, pairs_3, pairs_4, pairs_5]
    
class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['treatment'] = random.choice(['one', 'two'])
            p.treatment = p.participant.vars['treatment']

            if self.round_number == 1:
                axiomorder = []
                for x in range(5):
                    axiomorder.append(x)
                shuffle(axiomorder)
                p.participant.vars['axiomorder1'] = axiomorder[0]
                p.participant.vars['axiomorder2'] = axiomorder[1]
                p.participant.vars['axiomorder3'] = axiomorder[2]
                #p.participant.vars['axiomorder4'] = axiomorder[3]
                #p.participant.vars['axiomorder5'] = axiomorder[4]
            p.axiomord1 = p.participant.vars['axiomorder1']
            p.axiomord2 = p.participant.vars['axiomorder2']
            p.axiomord3 = p.participant.vars['axiomorder3']
            #p.axiomord4 = p.participant.vars['axiomorder4']
            #p.axiomord5 = p.participant.vars['axiomorder5']

            decorder = []
            for x in range(8):
                decorder.append(x)
            shuffle(decorder)
            p.decord1 = decorder[1]
            p.decord2 = decorder[2]
            p.decord3 = decorder[3]
            p.decord4 = decorder[4]
            p.decord5 = decorder[5]
            p.decord6 = decorder[6]
            p.decord7 = decorder[7]
            p.decord8 = decorder[0]

            p.axiomord = random.randint(0, 1)
            p.abord1 = random.randint(0, 1)
            p.abord2 = random.randint(0, 1)
            p.abord3 = random.randint(0, 1)
            p.abord4 = random.randint(0, 1)
            p.abord5 = random.randint(0, 1)
            p.abord6 = random.randint(0, 1)
            p.abord7 = random.randint(0, 1)
            p.abord8 = random.randint(0, 1)

            order = []
            for x in range(10):
                order.append(x)
            shuffle(order)
            p.ord0_1 = order[0]
            p.ord1_1 = order[1]
            p.ord2_1 = order[2]
            p.ord3_1 = order[3]
            p.ord4_1 = order[4]
            p.ord5_1 = order[5]
            p.ord6_1 = order[6]
            p.ord7_1 = order[7]
            p.ord8_1 = order[8]
            p.ord9_1 = order[9]
            shuffle(order)
            p.ord0_2 = order[0]
            p.ord1_2 = order[1]
            p.ord2_2 = order[2]
            p.ord3_2 = order[3]
            p.ord4_2 = order[4]
            p.ord5_2 = order[5]
            p.ord6_2 = order[6]
            p.ord7_2 = order[7]
            p.ord8_2 = order[8]
            p.ord9_2 = order[9]
            shuffle(order)
            p.ord0_3 = order[0]
            p.ord1_3 = order[1]
            p.ord2_3 = order[2]
            p.ord3_3 = order[3]
            p.ord4_3 = order[4]
            p.ord5_3 = order[5]
            p.ord6_3 = order[6]
            p.ord7_3 = order[7]
            p.ord8_3 = order[8]
            p.ord9_3 = order[9]
            shuffle(order)
            p.ord0_4 = order[0]
            p.ord1_4 = order[1]
            p.ord2_4 = order[2]
            p.ord3_4 = order[3]
            p.ord4_4 = order[4]
            p.ord5_4 = order[5]
            p.ord6_4 = order[6]
            p.ord7_4 = order[7]
            p.ord8_4 = order[8]
            p.ord9_4 = order[9]
            shuffle(order)
            p.ord0_5 = order[0]
            p.ord1_5 = order[1]
            p.ord2_5 = order[2]
            p.ord3_5 = order[3]
            p.ord4_5 = order[4]
            p.ord5_5 = order[5]
            p.ord6_5 = order[6]
            p.ord7_5 = order[7]
            p.ord8_5 = order[8]
            p.ord9_5 = order[9]
            shuffle(order)
            p.ord0_6 = order[0]
            p.ord1_6 = order[1]
            p.ord2_6 = order[2]
            p.ord3_6 = order[3]
            p.ord4_6 = order[4]
            p.ord5_6 = order[5]
            p.ord6_6 = order[6]
            p.ord7_6 = order[7]
            p.ord8_6 = order[8]
            p.ord9_6 = order[9]
            shuffle(order)
            p.ord0_7 = order[0]
            p.ord1_7 = order[1]
            p.ord2_7 = order[2]
            p.ord3_7 = order[3]
            p.ord4_7 = order[4]
            p.ord5_7 = order[5]
            p.ord6_7 = order[6]
            p.ord7_7 = order[7]
            p.ord8_7 = order[8]
            p.ord9_7 = order[9]
            shuffle(order)
            p.ord0_8 = order[0]
            p.ord1_8 = order[1]
            p.ord2_8 = order[2]
            p.ord3_8 = order[3]
            p.ord4_8 = order[4]
            p.ord5_8 = order[5]
            p.ord6_8 = order[6]
            p.ord7_8 = order[7]
            p.ord8_8 = order[8]
            p.ord9_8 = order[9]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    inconsistencies = models.IntegerField()

    def make_field2():
        return models.IntegerField(
            label="Please choose your commitment to the rule:",
            choices=[
                [1, 'I want to commit to the rule.'],
                [0, 'I do not want to commit, but rather decide case by case.'],
            ],
            widget=widgets.RadioSelect
        )
    axiom = make_field2()
    anti_axiom = make_field2()
    axiom_revised1 = make_field2()
    anti_axiom_revised1 = make_field2()
    axiom_revised2 = make_field2()
    anti_axiom_revised2 = make_field2()
    axiom_revised3 = make_field2()
    anti_axiom_revised3 = make_field2()

    def make_field():
        return models.IntegerField(
            label="Please choose which program should be implemented:",
            choices=[
                [0, 'I want program A to be implemented.'],
                [1, 'I want program B to be implemented.'],
            ],
            widget=widgets.RadioSelect
        )
    
    dec1 = make_field()
    dec2 = make_field()
    dec3 = make_field()
    dec4 = make_field()
    dec5 = make_field()
    dec6 = make_field()
    dec7 = make_field()
    dec8 = make_field()
    dec1_revised = make_field()
    dec2_revised = make_field()
    dec3_revised = make_field()
    dec4_revised = make_field()
    dec5_revised = make_field()
    dec6_revised = make_field()
    dec7_revised = make_field()
    dec8_revised = make_field()

    axiomord = models.IntegerField()
    axiomord1 = models.IntegerField()
    axiomord2 = models.IntegerField()
    axiomord3 = models.IntegerField()
    axiomord4 = models.IntegerField()
    axiomord5 = models.IntegerField()

    decord1 = models.IntegerField()
    decord2 = models.IntegerField()
    decord3 = models.IntegerField()
    decord4 = models.IntegerField()
    decord5 = models.IntegerField()
    decord6 = models.IntegerField()
    decord7 = models.IntegerField()
    decord8 = models.IntegerField()

    abord1 = models.IntegerField()
    abord2 = models.IntegerField()
    abord3 = models.IntegerField()
    abord4 = models.IntegerField()
    abord5 = models.IntegerField()
    abord6 = models.IntegerField()
    abord7 = models.IntegerField()
    abord8 = models.IntegerField()

    ord1_1 = models.IntegerField()
    ord2_1 = models.IntegerField()
    ord3_1 = models.IntegerField()
    ord4_1 = models.IntegerField()
    ord5_1 = models.IntegerField()
    ord6_1 = models.IntegerField()
    ord7_1 = models.IntegerField()
    ord8_1 = models.IntegerField()
    ord9_1 = models.IntegerField()
    ord0_1 = models.IntegerField()
    ord1_2 = models.IntegerField()
    ord2_2 = models.IntegerField()
    ord3_2 = models.IntegerField()
    ord4_2 = models.IntegerField()
    ord5_2 = models.IntegerField()
    ord6_2 = models.IntegerField()
    ord7_2 = models.IntegerField()
    ord8_2 = models.IntegerField()
    ord9_2 = models.IntegerField()
    ord0_2 = models.IntegerField()
    ord1_3 = models.IntegerField()
    ord2_3 = models.IntegerField()
    ord3_3 = models.IntegerField()
    ord4_3 = models.IntegerField()
    ord5_3 = models.IntegerField()
    ord6_3 = models.IntegerField()
    ord7_3 = models.IntegerField()
    ord8_3 = models.IntegerField()
    ord9_3 = models.IntegerField()
    ord0_3 = models.IntegerField()
    ord1_4 = models.IntegerField()
    ord2_4 = models.IntegerField()
    ord3_4 = models.IntegerField()
    ord4_4 = models.IntegerField()
    ord5_4 = models.IntegerField()
    ord6_4 = models.IntegerField()
    ord7_4 = models.IntegerField()
    ord8_4 = models.IntegerField()
    ord9_4 = models.IntegerField()
    ord0_4 = models.IntegerField()
    ord1_5 = models.IntegerField()
    ord2_5 = models.IntegerField()
    ord3_5 = models.IntegerField()
    ord4_5 = models.IntegerField()
    ord5_5 = models.IntegerField()
    ord6_5 = models.IntegerField()
    ord7_5 = models.IntegerField()
    ord8_5 = models.IntegerField()
    ord9_5 = models.IntegerField()
    ord0_5 = models.IntegerField()
    ord1_6 = models.IntegerField()
    ord2_6 = models.IntegerField()
    ord3_6 = models.IntegerField()
    ord4_6 = models.IntegerField()
    ord5_6 = models.IntegerField()
    ord6_6 = models.IntegerField()
    ord7_6 = models.IntegerField()
    ord8_6 = models.IntegerField()
    ord9_6 = models.IntegerField()
    ord0_6 = models.IntegerField()
    ord1_7 = models.IntegerField()
    ord2_7 = models.IntegerField()
    ord3_7 = models.IntegerField()
    ord4_7 = models.IntegerField()
    ord5_7 = models.IntegerField()
    ord6_7 = models.IntegerField()
    ord7_7 = models.IntegerField()
    ord8_7 = models.IntegerField()
    ord9_7 = models.IntegerField()
    ord0_7 = models.IntegerField()
    ord1_8 = models.IntegerField()
    ord2_8 = models.IntegerField()
    ord3_8 = models.IntegerField()
    ord4_8 = models.IntegerField()
    ord5_8 = models.IntegerField()
    ord6_8 = models.IntegerField()
    ord7_8 = models.IntegerField()
    ord8_8 = models.IntegerField()
    ord9_8 = models.IntegerField()
    ord0_8 = models.IntegerField()

    def check_inconsistencies(self) -> object:
        inconsistencies = []
        #decision index, axiom index, experiment decision index, decision
        if self.axiom == 1:
            if self.abord1 == 0 and self.dec1 == 1:
                inconsistencies.append([self.decord1, 1, 1, 1])
            if self.abord1 == 1 and self.dec1 == 0:
                inconsistencies.append([self.decord1, 1, 1, 0])
            if self.abord2 == 0 and self.dec2 == 1:
                inconsistencies.append([self.decord2, 1, 2, 1])
            if self.abord2 == 1 and self.dec2 == 0:
                inconsistencies.append([self.decord2, 1, 2, 0])
            if self.abord3 == 0 and self.dec3 == 1:
                inconsistencies.append([self.decord3, 1, 3, 1])
            if self.abord3 == 1 and self.dec3 == 0:
                inconsistencies.append([self.decord3, 1, 3, 0])
            if self.abord4 == 0 and self.dec4 == 1:
                inconsistencies.append([self.decord4, 1, 4, 1])
            if self.abord4 == 1 and self.dec4 == 0:
                inconsistencies.append([self.decord4, 1, 4, 0])
            if self.abord5 == 0 and self.dec5 == 1:
                inconsistencies.append([self.decord5, 1, 5, 1])
            if self.abord5 == 1 and self.dec5 == 0:
                inconsistencies.append([self.decord5, 1, 5, 0])
            if self.abord6 == 0 and self.dec6 == 1:
                inconsistencies.append([self.decord6, 1, 6, 1])
            if self.abord6 == 1 and self.dec6 == 0:
                inconsistencies.append([self.decord6, 1, 6, 0])
            if self.abord7 == 0 and self.dec7 == 1:
                inconsistencies.append([self.decord7, 1, 7, 1])
            if self.abord7 == 1 and self.dec7 == 0:
                inconsistencies.append([self.decord7, 1, 7, 0])
            if self.abord8 == 0 and self.dec8 == 1:
                inconsistencies.append([self.decord8, 1, 8, 1])
            if self.abord8 == 1 and self.dec8 == 0:
                inconsistencies.append([self.decord8, 1, 8, 0])
        if self.anti_axiom == 1:
            if self.abord1 == 0 and self.dec1 == 0:
                inconsistencies.append([self.decord1, 2, 1, 0])
            if self.abord1 == 1 and self.dec1 == 1:
                inconsistencies.append([self.decord1, 2, 1, 1])
            if self.abord2 == 0 and self.dec2 == 0:
                inconsistencies.append([self.decord2, 2, 2, 0])
            if self.abord2 == 1 and self.dec2 == 1:
                inconsistencies.append([self.decord2, 2, 2, 1])
            if self.abord3 == 0 and self.dec3 == 0:
                inconsistencies.append([self.decord3, 2, 3, 0])
            if self.abord3 == 1 and self.dec3 == 1:
                inconsistencies.append([self.decord3, 2, 3, 1])
            if self.abord4 == 0 and self.dec4 == 0:
                inconsistencies.append([self.decord4, 2, 4, 0])
            if self.abord4 == 1 and self.dec4 == 1:
                inconsistencies.append([self.decord4, 2, 4, 1])
            if self.abord5 == 0 and self.dec5 == 0:
                inconsistencies.append([self.decord5, 2, 5, 0])
            if self.abord5 == 1 and self.dec5 == 1:
                inconsistencies.append([self.decord5, 2, 5, 1])
            if self.abord6 == 0 and self.dec6 == 0:
                inconsistencies.append([self.decord6, 2, 6, 0])
            if self.abord6 == 1 and self.dec6 == 1:
                inconsistencies.append([self.decord6, 2, 6, 1])
            if self.abord7 == 0 and self.dec7 == 0:
                inconsistencies.append([self.decord7, 2, 7, 0])
            if self.abord7 == 1 and self.dec7 == 1:
                inconsistencies.append([self.decord7, 2, 7, 1])
            if self.abord8 == 0 and self.dec8 == 0:
                inconsistencies.append([self.decord8, 2, 8, 0])
            if self.abord8 == 1 and self.dec8 == 1:
                inconsistencies.append([self.decord8, 2, 8, 1])
        shuffle(inconsistencies)
        self.inconsistencies = len(inconsistencies)
        if self.inconsistencies > 0:
            self.participant.vars['inc1dec'] = inconsistencies[0][0]
            self.participant.vars['inc1axiom'] = inconsistencies[0][1]
            self.participant.vars['inc1ord'] = inconsistencies[0][2]
            self.participant.vars['inc1choice'] = inconsistencies[0][3]
        if self.inconsistencies > 1:
            self.participant.vars['inc2dec'] = inconsistencies[1][0]
            self.participant.vars['inc2axiom'] = inconsistencies[1][1]
            self.participant.vars['inc2ord'] = inconsistencies[1][2]
            self.participant.vars['inc2choice'] = inconsistencies[1][3]
        if self.inconsistencies > 2:
            self.participant.vars['inc3dec'] = inconsistencies[2][0]
            self.participant.vars['inc3axiom'] = inconsistencies[2][1]
            self.participant.vars['inc3ord'] = inconsistencies[2][2]
            self.participant.vars['inc3choice'] = inconsistencies[2][3]
        self.payoff = 0

