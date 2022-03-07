import main_stage as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        if self.participant.role == C.FIRM_ROLE:
            yield InfoRoleFirm
        if self.participant.role == C.OFFICIAL_ROLE:
            yield InfoRoleOfficial
        if self.player.self.participant.role == C.FIRM_ROLE:
            yield FirmChoice, dict(decision=True)
        if self.player.self.participant.role == C.OFFICIAL_ROLE:
            yield OfficialChoice, dict(decision=True)
        if self.player.round_number == C.NUM_ROUNDS:
            yield Feedback