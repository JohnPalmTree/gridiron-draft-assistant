"""
Name: GRIDIRON.py
Author: John 🌴
Start Date: 2/22/26
Purpose: The main engine for the GRIDIRON Draft Assistant.
"""

def selectEntry(msg):
    x = input(msg)

    return x

def promptLeagueSettingsEdit(): # clean up - getSetting fct, getPositionNumber(pos), data validation
    if selectEntry("Would you like to edit league settings? [Y/N]\n") == "Y":
        leagueSettings['num_teams'] = int(input("Enter the number of teams in your league:\n"))
        leagueSettings['ppr'] = float(input("Enter the points per reception for your league. (0, 0.5, or 1):\n"))

        if selectEntry("\nWould you like to edit roster settings? [Y/N]\n") == "Y":
            for posName, posNum in leagueSettings['starters'].items():
                raw = input(f"Enter the # of {posName.upper()} that you are able to start:\n").strip() # prompt input and strip whitespaces

                leagueSettings['starters'][posName] = int(raw)

            leagueSettings['bench'] = int(input('Enter the # of players you are able to bench. [default: 6]:\n'))
            
            if selectEntry("\nCan you use QBs in your FLEX position? [Y/N]\n") == "Y":
                leagueSettings['superflex'] = 1
            else:
                leagueSettings['superflex'] = 0

    print(leagueSettings)

def loadPlayers():
    print("Beginning player loading...")



def init():
    print("Beginning loop process...")

    promptLeagueSettingsEdit()

    loadPlayers()

    # plrs = load players from .csv's

    # for each plr, calculate expected points ((.75 * projFPTS) + (.25*lastYearPPG))

    # calcReplacementRanks(Settings): 
        # let T be num_Teams and S be the dict. of starters
        # let flex_total be T * S.get('flex', 0)
                
        # calculate demand for each position - [T * S.get("QB", 0)] OR [(T * S.get(pos, 0) + flex_total * settings.flex_allocation[pos])]

        # calcCutoff = {pos: math.ceil(demand[pos] for pos in demand)}
        # repl_rank = {pos: cutoff[pos] + settings.buffer[pos] for pos in cutoff}

        # return repl_rank

    # calcReplacementPoints(plrs, settings):
        # repl_rank = calcReplacementRanks(settings)
        # repl_points = {}

        # for each pos,
            # get the players for the specific position, and sort them based on expected points
            # index = repl_rank[pos] - 1 (0-index)
            # if the plrs for the pos is empty, 
                # return 0 replacement points.
            # otherwise, if the index is >= the num of plrs in position,
                # repl_points[pos] = pos_players[-1].exp_pts
            # otherwise,
                # repl_points[pos] = pos_players[idx].exp_pts

        # return repl_points

    # gradePlayers(plrs, repl_points):
        # VOR:
            # for each plr,
                # p.vor = p.exp_pts - replacement_points[p.pos]
        # Grade: scale VOR to 0..100 using min/max across all players

        # return sorted array of plrs

    # create draft board - loop through every player and give them a grade. read in via .csv sheets for each position. 
        # gradePlayers(Plr, repl_points)

    # show initial board
        # print_top(board, n=25)

    # start draft - import league settings and handle things like pick_number and available_players. allow players to pick which draft position is theirs to have their team stand out.
        # pick(plr) functionality - will have to manually pick for every team


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
    'superflex': 0,
    'flex_eligibility': {'rb', 'wr', 'te'},
    'superflex_eligibility': {'qb', 'rb', 'wr', 'te'},
    'flex_allocation': {'rb': 0.40, 'wr': 0.55, 'te': 0.05},
    'buffer': {'qb': 6, 'rb': 12, 'wr': 12, 'te': 6},
}

init()
