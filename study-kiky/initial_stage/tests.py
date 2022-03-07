import initial_stage as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number == 1:
            yield AdditionalInfo
        if self.player.role == C.FIRM_ROLE:
            yield FirmChoice, dict(firm_offer=True)
        if self.player.role == C.OFFICIAL_ROLE:
            yield OfficialChoice, dict(official_accept=False)
        if self.player.round_number == C.NUM_ROUNDS:
            yield Feedback