import Post_survey as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        yield Demographics, dict(
            age=125,
            gender="Male",
            job="Employed full-time",
            work_experience=0,
            religion="None",
            nationality="Afghan",
            other_country=1,
            time_spent_other_country=0,
            testi=1,
            testi2=1,
            check1=True,
            check2=1,
        )
        yield Payment