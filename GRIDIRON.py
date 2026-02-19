"""
Docstring for GRIDIRON

init()
    prompt league setting entry
    startDraft()


"""

def promptLeagueSettingsEdit():
    print("Enter [Y] to edit league settings.")
    
    


def init():
    print("Beginning loop process...")

    # prompt enter league settings - if true, handle that
        # would you liked to edit num_teams? draft? ppr? starters? have to 

leagueSettings = {
    'num_teams': 12,
    'draft': 'snake',
    'ppr': 1.0,
    'starters': {
        'qb': 1,
        'rb': 2,
        'wr': 2,
        'te': 1,
        'flex': 1,
    },
    'bench': 6,
    'flex_eligibility': {'rb', 'wr', 'te'},
}

init()