class ProjectionRank:
    '''store all projection stats for a team'''
    def __init__(self):
        self.exp_wins         = 1.
        self.div_win_pct      = 1.
        self.wild_card_pct    = 1.
        self.make_playoff_pct = 1.
        self.overall          = 1.
    def __repr__(self):
        print('           Exp. Wins : %.3f'%self.exp_wins)
        print('     Div. Winner (%) : %.3f'%self.div_win_pct)
        print('       Wild Card (%) : %.3f'%self.wild_card_pct)
        print('   Make Playoffs (%) : %.3f'%self.make_playoff_pct)
        print('             Overall : %.3f'%self.overall)
