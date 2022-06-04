from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
from app import db 

class player_allstar(db.Model):
	__tablename__ = "player_allstar"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'),primary_key=True)
	last_name = db.Column(db.DateTime)
	first_name = db.Column(db.String(300))
	season_id = db.Column(db.String(300))
	conference = db.Column(db.String(300))
	league_id = db.Column(db.String(300))
	games_played = db.Column(db.String(300))
	minutes = db.Column(db.String(300))
	points = db.Column(db.String(300))
	o_rebounds = db.Column(db.String(300))
	d_rebounds = db.Column(db.String(300))
	rebounds = db.Column(db.String(300))
	assists = db.Column(db.String(300))
	steals = db.Column(db.String(300))
	blocks = db.Column(db.String(300))
	turnovers = db.Column(db.String(300))
	personal_fouls = db.Column(db.String(300))
	fg_attempted = db.Column(db.String(300))
	fg_made = db.Column(db.String(300))
	ft_attempted = db.Column(db.String(300))
	ft_made = db.Column(db.String(300))
	three_attempted = db.Column(db.String(300))
	three_made = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"last_name": self.last_name,
			"first_name": self.first_name,
			"season_id": self.season_id,
			"conference": self.conference,
			"league_id": self.league_id,
			"games_played": self.games_played,
			"minutes": self.minutes,
			"points": self.points,
			"o_rebounds": self.o_rebounds,
			"d_rebounds": self.d_rebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"personal_fouls": self.personal_fouls,
			"fg_attempted": self.fg_attempted,
			"fg_made": self.fg_made,
			"ft_attempted": self.ft_attempted,
			"ft_made": self.ft_made,
			"three_attempted": self.three_attempted,
			"three_made": self.three_made,
		}
