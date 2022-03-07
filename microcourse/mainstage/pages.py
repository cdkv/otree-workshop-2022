from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class NextRoundPage(Page):
    def is_displayed(self):
        return self.round_number > 1

class AxiomInstructionPage(Page):
    pass

class AxiomPage1(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.axiomord == 0:
            return ['axiom']
        else:
            return ['anti_axiom']

    def vars_for_template(self):
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        if self.player.axiomord == 0:
            axiom_text = Constants.all_axioms[axiom][0]
        else:
            axiom_text = Constants.all_axioms[axiom][1]
        return dict(
            axiom_text=axiom_text,
        )

class AxiomPage2(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.axiomord == 1:
            return ['axiom']
        else:
            return ['anti_axiom']

    def vars_for_template(self):
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        if self.player.axiomord == 0:
            axiom_text = Constants.all_axioms[axiom][1]
        else:
            axiom_text = Constants.all_axioms[axiom][0]
        return dict(
            axiom_text=axiom_text,
        )

class DecInstructionPage(Page):
    pass

class DecisionPage1(Page):
    form_model = 'player'
    form_fields = ['dec1']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord1_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord2_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord3_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord4_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord5_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord6_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord7_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord8_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord9_1])
        data.append(Constants.all_pairs[axiom][self.player.decord1][self.player.ord0_1])
        data_a = []
        data_b = []
        if self.player.abord1 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord1 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage2(Page):
    form_model = 'player'
    form_fields = ['dec2']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord1_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord2_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord3_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord4_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord5_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord6_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord7_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord8_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord9_2])
        data.append(Constants.all_pairs[axiom][self.player.decord2][self.player.ord0_2])
        data_a = []
        data_b = []
        if self.player.abord2 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord2 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage3(Page):
    form_model = 'player'
    form_fields = ['dec3']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord1_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord2_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord3_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord4_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord5_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord6_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord7_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord8_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord9_3])
        data.append(Constants.all_pairs[axiom][self.player.decord3][self.player.ord0_3])
        data_a = []
        data_b = []
        if self.player.abord3 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord3 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage4(Page):
    form_model = 'player'
    form_fields = ['dec4']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord1_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord2_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord3_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord4_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord5_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord6_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord7_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord8_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord9_4])
        data.append(Constants.all_pairs[axiom][self.player.decord4][self.player.ord0_4])
        data_a = []
        data_b = []
        if self.player.abord4 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord4 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage5(Page):
    form_model = 'player'
    form_fields = ['dec5']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord1_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord2_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord3_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord4_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord5_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord6_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord7_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord8_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord9_5])
        data.append(Constants.all_pairs[axiom][self.player.decord5][self.player.ord0_5])
        data_a = []
        data_b = []
        if self.player.abord5 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord5 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage6(Page):
    form_model = 'player'
    form_fields = ['dec6']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord1_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord2_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord3_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord4_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord5_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord6_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord7_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord8_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord9_6])
        data.append(Constants.all_pairs[axiom][self.player.decord6][self.player.ord0_6])
        data_a = []
        data_b = []
        if self.player.abord6 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord6 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage7(Page):
    form_model = 'player'
    form_fields = ['dec7']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord1_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord2_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord3_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord4_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord5_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord6_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord7_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord8_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord9_7])
        data.append(Constants.all_pairs[axiom][self.player.decord7][self.player.ord0_7])
        data_a = []
        data_b = []
        if self.player.abord7 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord7 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

class DecisionPage8(Page):
    form_model = 'player'
    form_fields = ['dec8']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord1_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord2_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord3_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord4_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord5_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord6_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord7_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord8_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord9_8])
        data.append(Constants.all_pairs[axiom][self.player.decord8][self.player.ord0_8])
        data_a = []
        data_b = []
        if self.player.abord8 == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if self.player.abord8 == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        return dict(
            data_a=data_a,
            data_b=data_b,
        )

    def before_next_page(self):
        self.player.check_inconsistencies()

class RevInstructionPage(Page):
    def is_displayed(self):
        return self.player.inconsistencies > 0


class RevisionPage1(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.participant.vars['inc1axiom'] == 1:
            return ['axiom_revised1', 'dec1_revised']
        else:
            return ['anti_axiom_revised1', 'dec1_revised']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        decision_order = self.player.participant.vars['inc1dec']
        xp_dec_order = self.player.participant.vars['inc1ord']
        pairorder = []
        if xp_dec_order == 1:
            aborder = self.player.abord1
            pairorder = [self.player.ord1_1, self.player.ord2_1, self.player.ord3_1, self.player.ord4_1, self.player.ord5_1, self.player.ord6_1, self.player.ord7_1, self.player.ord8_1, self.player.ord9_1, self.player.ord0_1]
        if xp_dec_order == 2:
            aborder = self.player.abord2
            pairorder = [self.player.ord1_2, self.player.ord2_2, self.player.ord3_2, self.player.ord4_2, self.player.ord5_2, self.player.ord6_2, self.player.ord7_2, self.player.ord8_2, self.player.ord9_2, self.player.ord0_2]
        if xp_dec_order == 3:
            aborder = self.player.abord3
            pairorder = [self.player.ord1_3, self.player.ord2_3, self.player.ord3_3, self.player.ord4_3, self.player.ord5_3, self.player.ord6_3, self.player.ord7_3, self.player.ord8_3, self.player.ord9_3, self.player.ord0_3]
        if xp_dec_order == 4:
            aborder = self.player.abord4
            pairorder = [self.player.ord1_4, self.player.ord2_4, self.player.ord3_4, self.player.ord4_4, self.player.ord5_4, self.player.ord6_4, self.player.ord7_4, self.player.ord8_4, self.player.ord9_4, self.player.ord0_4]
        if xp_dec_order == 5:
            aborder = self.player.abord5
            pairorder = [self.player.ord1_5, self.player.ord2_5, self.player.ord3_5, self.player.ord4_5, self.player.ord5_5, self.player.ord6_5, self.player.ord7_5, self.player.ord8_5, self.player.ord9_5, self.player.ord0_5]
        if xp_dec_order == 6:
            aborder = self.player.abord6
            pairorder = [self.player.ord1_6, self.player.ord2_6, self.player.ord3_6, self.player.ord4_6, self.player.ord5_6, self.player.ord6_6, self.player.ord7_6, self.player.ord8_6, self.player.ord9_6, self.player.ord0_6]
        if xp_dec_order == 7:
            aborder = self.player.abord7
            pairorder = [self.player.ord1_7, self.player.ord2_7, self.player.ord3_7, self.player.ord4_7, self.player.ord5_7, self.player.ord6_7, self.player.ord7_7, self.player.ord8_7, self.player.ord9_7, self.player.ord0_7]
        if xp_dec_order == 8:
            aborder = self.player.abord8
            pairorder = [self.player.ord1_8, self.player.ord2_8, self.player.ord3_8, self.player.ord4_8, self.player.ord5_8, self.player.ord6_8, self.player.ord7_8, self.player.ord8_8, self.player.ord9_8, self.player.ord0_8]
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[0]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[1]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[2]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[3]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[4]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[5]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[6]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[7]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[8]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[9]])
        data_a = []
        data_b = []
        if aborder == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if aborder == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        if self.player.participant.vars['inc1axiom'] == 1:
            axiom_text = Constants.all_axioms[axiom][0]
        else:
            axiom_text = Constants.all_axioms[axiom][1]
        if self.player.participant.vars['inc1choice'] == 0:
            choice = 'A'
        else:
            choice = 'B'
        return dict(
            axiom_text=axiom_text,
            data_a=data_a,
            data_b=data_b,
            choice=choice,
        )

    def is_displayed(self):
        return self.player.inconsistencies > 0


class RevisionPage2(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.participant.vars['inc2axiom'] == 1:
            return ['axiom_revised2', 'dec2_revised']
        else:
            return ['anti_axiom_revised2', 'dec2_revised']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        decision_order = self.player.participant.vars['inc2dec']
        xp_dec_order = self.player.participant.vars['inc2ord']
        pairorder = []
        if xp_dec_order == 1:
            aborder = self.player.abord1
            pairorder = [self.player.ord1_1, self.player.ord2_1, self.player.ord3_1, self.player.ord4_1, self.player.ord5_1, self.player.ord6_1, self.player.ord7_1, self.player.ord8_1, self.player.ord9_1, self.player.ord0_1]
        if xp_dec_order == 2:
            aborder = self.player.abord2
            pairorder = [self.player.ord1_2, self.player.ord2_2, self.player.ord3_2, self.player.ord4_2, self.player.ord5_2, self.player.ord6_2, self.player.ord7_2, self.player.ord8_2, self.player.ord9_2, self.player.ord0_2]
        if xp_dec_order == 3:
            aborder = self.player.abord3
            pairorder = [self.player.ord1_3, self.player.ord2_3, self.player.ord3_3, self.player.ord4_3, self.player.ord5_3, self.player.ord6_3, self.player.ord7_3, self.player.ord8_3, self.player.ord9_3, self.player.ord0_3]
        if xp_dec_order == 4:
            aborder = self.player.abord4
            pairorder = [self.player.ord1_4, self.player.ord2_4, self.player.ord3_4, self.player.ord4_4, self.player.ord5_4, self.player.ord6_4, self.player.ord7_4, self.player.ord8_4, self.player.ord9_4, self.player.ord0_4]
        if xp_dec_order == 5:
            aborder = self.player.abord5
            pairorder = [self.player.ord1_5, self.player.ord2_5, self.player.ord3_5, self.player.ord4_5, self.player.ord5_5, self.player.ord6_5, self.player.ord7_5, self.player.ord8_5, self.player.ord9_5, self.player.ord0_5]
        if xp_dec_order == 6:
            aborder = self.player.abord6
            pairorder = [self.player.ord1_6, self.player.ord2_6, self.player.ord3_6, self.player.ord4_6, self.player.ord5_6, self.player.ord6_6, self.player.ord7_6, self.player.ord8_6, self.player.ord9_6, self.player.ord0_6]
        if xp_dec_order == 7:
            aborder = self.player.abord7
            pairorder = [self.player.ord1_7, self.player.ord2_7, self.player.ord3_7, self.player.ord4_7, self.player.ord5_7, self.player.ord6_7, self.player.ord7_7, self.player.ord8_7, self.player.ord9_7, self.player.ord0_7]
        if xp_dec_order == 8:
            aborder = self.player.abord8
            pairorder = [self.player.ord1_8, self.player.ord2_8, self.player.ord3_8, self.player.ord4_8, self.player.ord5_8, self.player.ord6_8, self.player.ord7_8, self.player.ord8_8, self.player.ord9_8, self.player.ord0_8]
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[0]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[1]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[2]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[3]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[4]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[5]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[6]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[7]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[8]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[9]])
        data_a = []
        data_b = []
        if aborder == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if aborder == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        if self.player.participant.vars['inc2axiom'] == 1:
            axiom_text = Constants.all_axioms[axiom][0]
        else:
            axiom_text = Constants.all_axioms[axiom][1]
        if self.player.participant.vars['inc2choice'] == 0:
            choice = 'A'
        else:
            choice = 'B'
        return dict(
            axiom_text=axiom_text,
            data_a=data_a,
            data_b=data_b,
            choice=choice,
        )

    def is_displayed(self):
        return self.player.inconsistencies > 1

class RevisionPage3(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.participant.vars['inc3axiom'] == 1:
            return ['axiom_revised3', 'dec3_revised']
        else:
            return ['anti_axiom_revised3', 'dec3_revised']

    def vars_for_template(self):
        data=[]
        if self.round_number == 1:
            axiom = self.player.axiomord1
        if self.round_number == 2:
            axiom = self.player.axiomord2
        if self.round_number == 3:
            axiom = self.player.axiomord3
        if self.round_number == 4:
            axiom = self.player.axiomord4
        if self.round_number == 5:
            axiom = self.player.axiomord5
        decision_order = self.player.participant.vars['inc3dec']
        xp_dec_order = self.player.participant.vars['inc3ord']
        pairorder = []
        if xp_dec_order == 1:
            aborder = self.player.abord1
            pairorder = [self.player.ord1_1, self.player.ord2_1, self.player.ord3_1, self.player.ord4_1, self.player.ord5_1, self.player.ord6_1, self.player.ord7_1, self.player.ord8_1, self.player.ord9_1, self.player.ord0_1]
        if xp_dec_order == 2:
            aborder = self.player.abord2
            pairorder = [self.player.ord1_2, self.player.ord2_2, self.player.ord3_2, self.player.ord4_2, self.player.ord5_2, self.player.ord6_2, self.player.ord7_2, self.player.ord8_2, self.player.ord9_2, self.player.ord0_2]
        if xp_dec_order == 3:
            aborder = self.player.abord3
            pairorder = [self.player.ord1_3, self.player.ord2_3, self.player.ord3_3, self.player.ord4_3, self.player.ord5_3, self.player.ord6_3, self.player.ord7_3, self.player.ord8_3, self.player.ord9_3, self.player.ord0_3]
        if xp_dec_order == 4:
            aborder = self.player.abord4
            pairorder = [self.player.ord1_4, self.player.ord2_4, self.player.ord3_4, self.player.ord4_4, self.player.ord5_4, self.player.ord6_4, self.player.ord7_4, self.player.ord8_4, self.player.ord9_4, self.player.ord0_4]
        if xp_dec_order == 5:
            aborder = self.player.abord5
            pairorder = [self.player.ord1_5, self.player.ord2_5, self.player.ord3_5, self.player.ord4_5, self.player.ord5_5, self.player.ord6_5, self.player.ord7_5, self.player.ord8_5, self.player.ord9_5, self.player.ord0_5]
        if xp_dec_order == 6:
            aborder = self.player.abord6
            pairorder = [self.player.ord1_6, self.player.ord2_6, self.player.ord3_6, self.player.ord4_6, self.player.ord5_6, self.player.ord6_6, self.player.ord7_6, self.player.ord8_6, self.player.ord9_6, self.player.ord0_6]
        if xp_dec_order == 7:
            aborder = self.player.abord7
            pairorder = [self.player.ord1_7, self.player.ord2_7, self.player.ord3_7, self.player.ord4_7, self.player.ord5_7, self.player.ord6_7, self.player.ord7_7, self.player.ord8_7, self.player.ord9_7, self.player.ord0_7]
        if xp_dec_order == 8:
            aborder = self.player.abord8
            pairorder = [self.player.ord1_8, self.player.ord2_8, self.player.ord3_8, self.player.ord4_8, self.player.ord5_8, self.player.ord6_8, self.player.ord7_8, self.player.ord8_8, self.player.ord9_8, self.player.ord0_8]
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[0]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[1]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[2]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[3]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[4]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[5]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[6]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[7]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[8]])
        data.append(Constants.all_pairs[axiom][decision_order][pairorder[9]])
        data_a = []
        data_b = []
        if aborder == 0:
            for x in range(10):
                data_a.append(data[x][0])
                data_b.append(data[x][1])
        if aborder == 1:
            for x in range(10):
                data_a.append(data[x][1])
                data_b.append(data[x][0])
        if self.player.participant.vars['inc3axiom'] == 1:
            axiom_text = Constants.all_axioms[axiom][0]
        else:
            axiom_text = Constants.all_axioms[axiom][1]
        if self.player.participant.vars['inc3choice'] == 0:
            choice = 'A'
        else:
            choice = 'B'
        return dict(
            axiom_text=axiom_text,
            data_a=data_a,
            data_b=data_b,
            choice=choice,
        )

    def is_displayed(self):
        return self.player.inconsistencies > 2

page_sequence = [NextRoundPage, AxiomInstructionPage, AxiomPage1, AxiomPage2, DecInstructionPage, DecisionPage1, DecisionPage2, DecisionPage3, DecisionPage4, DecisionPage5, DecisionPage6, DecisionPage7, DecisionPage8, RevInstructionPage, RevisionPage1, RevisionPage2, RevisionPage3]

