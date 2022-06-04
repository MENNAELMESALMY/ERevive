
testSchema = {
    1: 
    {'TableName': 'awards_coaches', 
        'TableType':'',
        'attributes': {
        'id': 'str', 
        'coachID': 'datetime',
        'award': 'str',
        'lgID': 'str',
        'note': 'str',
        }, 
        'primaryKey': ['id'], 
        'ForgeinKey': [
        {
        'attributeName': 'coachID',
        'ForignKeyTable': 'coaches', 
        'ForignKeyTableAttributeName': 'coachID', 
        'patricipaction': 'partial', 
        'dataType': 'str'},
        ], 
        'isWeak': False
    },
    2: 
    {
        'TableName': 'awards_players', 
        'TableType':'',
        'attributes': {
        'playerID': 'str', 
        'award': 'str',
        'year': 'int',
        'lgID': 'str',
        'note': 'str',
        'pos': 'str'
        }
        , 
        'primaryKey': ['name','year','lgID']
        , 
        'ForgeinKey': [
        {
        'attributeName': 'playerID',
        'ForignKeyTable': 'players', 
        'ForignKeyTableAttributeName': 'playerID', 
        'patricipaction': 'partial', 
        'dataType': 'str'
        }
        ], 
        'isWeak': False
    },
    5:
    {
        'TableName': 'player_allstar', 
        'TableType':'',
        'attributes': {
        'playerID': 'str', 
        'last_name': 'datetime',
        'first_name': 'str',
        'season_id': 'str',
        'conference': 'str',
        'league_id': 'str',
        'games_played': 'str',
        'minutes': 'str',
        'points': 'str',
        'o_rebounds': 'str',
        'd_rebounds': 'str',
        'rebounds': 'str',
        'assists': 'str',
        'steals': 'str',
        'blocks': 'str',
        'turnovers': 'str',
        'personal_fouls': 'str',
        'fg_attempted': 'str',
        'fg_made': 'str',
        'ft_attempted': 'str',
        'ft_made': 'str',
        'three_attempted':  'str',
        'three_made': 'str',
        }, 
        'primaryKey': ['playerID'], 
        'ForgeinKey': [
        {
        'attributeName': 'playerID',
        'ForignKeyTable': 'players', 
        'ForignKeyTableAttributeName': 'playerID', 
        'patricipaction': 'partial', 
        'dataType': 'str'},
        ], 
        'isWeak': False
    },
    3:
    {
        'TableName': 'players', 
        'TableType':'',
        'attributes': {
        'playerID' : 'str',
        'useFirst' : 'str',
        'firstName' : 'str',
        'middleName' : 'str',
        'lastName' : 'str',
        'nameGiven' : 'str',
        'fullGivenName' : 'str',
        'nameSuffix' : 'str',
        'nameNick' : 'str',
        'pos' : 'str',
        'firstseason' : 'int',
        'lastseason' : 'int',
        'height' :'float',
        'weight' : 'int',
        'college' : 'str',
        'collegeOther' : 'str',
        'birthDate': 'datetime',
        'birthCity' : 'str',
        'birthState' : 'str',
        'birthCountry' : 'str',
        'highSchool' : 'str',
        'hsCity' : 'str',
        'hsState' : 'str',
        'hsCountry' : 'str',
        'deathDate': 'datetime',
        'race' : 'str',
        }
        , 
        'primaryKey': ['playerID']
        , 
        'ForgeinKey': [], 
        'isWeak': False
    },
    4:{
        'TableName': 'coaches',
        'TableType':'',
        'attributes': {
        'coachID': 'str', 
        'year': 'int',
        'tmID': 'str',
        'lgID': 'str',
        'stint': 'int',
        'won': 'int',
        'lost': 'int',
        'post_wins': 'int',
        'post_losses': 'int'},
        'primaryKey': ['coachID','year','tmID','stint'],
        'ForgeinKey': [
        # {
        # 'attributeName': 'tmID',
        # 'ForignKeyTable': 'teams', 
        # 'ForignKeyTableAttributeName': 'tmID', 
        # 'patricipaction': 'partial', 
        # 'dataType': 'str'}
        ]
    },
    6: 
    {
        'TableName': 'players_teams', 
        'TableType':'',
        'attributes': {
        'id' : 'int',
        'playerID' : 'str',
        'year' : 'int',
        'stint' : 'int',
        'tmID' : 'str',
        'lgID' : 'str',
        'GP' : 'int',
        'GS' : 'int',
        'minutes' : 'int',
        'points' : 'int',
        'oRebounds' : 'int',
        'dRebounds' : 'int',
        'rebounds' : 'int',
        'assists' : 'int',
        'steals' : 'int',
        'blocks' : 'int',
        'turnovers' : 'int',
        'PF' : 'int',
        'fgAttempted' : 'int',
        'fgMade' : 'int',
        'ftAttempted' : 'int',
        'ftMade' : 'int',
        'threeAttempted' : 'int',
        'threeMade' : 'int',
        'PostGP' : 'int',
        'PostGS' : 'int',
        'PostMinutes' : 'int',
        'PostPoints' : 'int',
        'PostoRebounds' : 'int',
        'PostdRebounds' : 'int',
        'PostRebounds' : 'int',
        'PostAssists' : 'int',
        'PostSteals' : 'int',
        'PostBlocks' : 'int',
        'PostTurnovers' : 'int',
        'PostPF' : 'int',
        'PostfgAttempted' : 'int',
        'PostfgMade' : 'int',
        'PostftAttempted' : 'int',
        'PostftMade' : 'int',
        'PostthreeAttempted' : 'int',
        'PostthreeMade' : 'int',
        'note' : 'str',
            }
            , 
            'primaryKey': ['id']
            , 
            'ForgeinKey': [
            {
            'attributeName': 'playerID',
            'ForignKeyTable': 'players', 
            'ForignKeyTableAttributeName': 'playerID', 
            'patricipaction': 'partial', 
            'dataType': 'str'
            },
            {
            'attributeName': 'tmID',
            'ForignKeyTable': 'teams', 
            'ForignKeyTableAttributeName': 'tmID',
            'patricipaction': 'partial', 
            'dataType': 'str'
            }
            ], 
            'isWeak': False
    },
    7: 
    {
        'TableName': 'draft', 
        'TableType':'',
        'attributes': 
        {'id': 'str', 
        'draftYear': 'datetime',
        'draftRound': 'str',
        'draftSelection':'str',
        'draftOverall': 'datetime',
        'tmID': 'str',
        'firstName':'str',
        'lastName':'str',
        'suffixName':'str',
        'playerID':'str',
        'draftForm':'str',
        'lgID':'str',
        }, 
        'primaryKey': ['id'], 
        'ForgeinKey': 
            [{'attributeName': 'tmID',
            'ForignKeyTable': 'teams', 
            'ForignKeyTableAttributeName': 'tmID', 
            'patricipaction': 'partial', 
            'dataType': 'str'},
            {'attributeName': 'draftYear',
            'ForignKeyTable': 'teams', 
            'ForignKeyTableAttributeName': 'year', 
            'patricipaction': 'partial', 
            'dataType': 'str'}
            ], 
        'isWeak': False
    },
    8: 
    {
        'TableName': 'series_post', 
        'TableType':'',
        'attributes': 
            {'id': 'str',
            'year': 'str',
            'round': 'str',
            'series': 'str',
            'tmIDWinner': 'str',
            'lgIDWinner': 'str',
            'tmIDLoser': 'str',
            'lgIDLoser': 'str',
            'w': 'str',
            'L': 'str',}, 
        'primaryKey': ['id'], 
        'ForgeinKey': 
            [{'attributeName': 'tmIDWinner', 
            'ForignKeyTable': 'teams', 
            'ForignKeyTableAttributeName': 'tmID', 
            'patricipaction': 'full', 
            'dataType': 'str'},
            {'attributeName': 'tmIDLoser', 
            'ForignKeyTable': 'teams', 
            'ForignKeyTableAttributeName': 'tmID', 
            'patricipaction': 'full', 
            'dataType': 'str'},
            {'attributeName': 'year', 
            'ForignKeyTable': 'teams', 
            'ForignKeyTableAttributeName': 'year', 
            'patricipaction': 'full', 
            'dataType': 'str'},
            ], 
        'isWeak': False
    },
    9:{
        'TableName': 'teams',
        'TableType':'',
        'attributes': {
            'year': 'int',
        'lgID' :'str',
        'tmID' : 'str',
        'franchID' : 'str',
        'confID': 'str',
        'divID': 'str',
        'rank' :'int',
        'confRank': 'int',
        'playoff': 'str',
        'name' : 'str',
                },
                'primaryKey': ['year','tmID'],
                'ForgeinKey': []
    }

}

import pickle
with open('/home/nada/GP/GP/src/TestSchemas/sportsSchema.pickle', 'wb') as handle:
    pickle.dump(testSchema, handle, protocol=pickle.HIGHEST_PROTOCOL)
