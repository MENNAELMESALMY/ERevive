from .awards_coaches_api import awards_coaches_namespace 
from .awards_players_api import awards_players_namespace 
from .player_allstar_api import player_allstar_namespace 
from .players_api import players_namespace 
from .coaches_api import coaches_namespace 
from .players_teams_api import players_teams_namespace 
from .draft_api import draft_namespace 
from .series_post_api import series_post_namespace 
from .teams_api import teams_namespace 
from .players_awards_players_api import players_awards_players_namespace 
from .players_awards_coaches_api import players_awards_coaches_namespace 
from .players_teams_teams_api import players_teams_teams_namespace 
from .players_coaches_api import players_coaches_namespace 
from .awards_coaches_coaches_players_api import awards_coaches_coaches_players_namespace 
from .awards_coaches_series_post_api import awards_coaches_series_post_namespace 
from .awards_coaches_series_post_coaches_api import awards_coaches_series_post_coaches_namespace 
from .series_post_coaches_api import series_post_coaches_namespace 
from .coaches_awards_coaches_api import coaches_awards_coaches_namespace 
from .awards_players_player_allstar_api import awards_players_player_allstar_namespace 
from .awards_players_teams_api import awards_players_teams_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(awards_coaches_namespace,path="/awards_coaches")
    rest_plus_api.add_namespace(awards_players_namespace,path="/awards_players")
    rest_plus_api.add_namespace(player_allstar_namespace,path="/player_allstar")
    rest_plus_api.add_namespace(players_namespace,path="/players")
    rest_plus_api.add_namespace(coaches_namespace,path="/coaches")
    rest_plus_api.add_namespace(players_teams_namespace,path="/players_teams")
    rest_plus_api.add_namespace(draft_namespace,path="/draft")
    rest_plus_api.add_namespace(series_post_namespace,path="/series_post")
    rest_plus_api.add_namespace(teams_namespace,path="/teams")
    
    rest_plus_api.add_namespace(players_awards_players_namespace,path="/players/awards_players")
    rest_plus_api.add_namespace(players_awards_coaches_namespace,path="/players/awards_coaches")
    rest_plus_api.add_namespace(players_teams_teams_namespace,path="/players_teams/teams")
    rest_plus_api.add_namespace(players_coaches_namespace,path="/players/coaches")
    rest_plus_api.add_namespace(awards_coaches_coaches_players_namespace,path="/awards_coaches/coaches/players")
    rest_plus_api.add_namespace(awards_coaches_series_post_namespace,path="/awards_coaches/series_post")
    rest_plus_api.add_namespace(awards_coaches_series_post_coaches_namespace,path="/awards_coaches/series_post/coaches")
    rest_plus_api.add_namespace(series_post_coaches_namespace,path="/series_post/coaches")
    rest_plus_api.add_namespace(coaches_awards_coaches_namespace,path="/coaches/awards_coaches")
    rest_plus_api.add_namespace(awards_players_player_allstar_namespace,path="/awards_players/player_allstar")
    rest_plus_api.add_namespace(awards_players_teams_namespace,path="/awards_players/teams")
    return rest_plus_api