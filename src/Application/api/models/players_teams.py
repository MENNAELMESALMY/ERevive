from app import db 

class players_teams(db.Model):
	__tablename__ = "players_teams"
	id = db.Column(db.Integer,unique=True,primary_key=True)
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'))
	year = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	tmID = db.Column(db.String(300),db.ForeignKey('teams.tmID'))
	lgID = db.Column(db.String(300))
	GP = db.Column(db.Integer)
	GS = db.Column(db.Integer)
	minutes = db.Column(db.Integer)
	points = db.Column(db.Integer)
	oRebounds = db.Column(db.Integer)
	dRebounds = db.Column(db.Integer)
	rebounds = db.Column(db.Integer)
	assists = db.Column(db.Integer)
	steals = db.Column(db.Integer)
	blocks = db.Column(db.Integer)
	turnovers = db.Column(db.Integer)
	PF = db.Column(db.Integer)
	fgAttempted = db.Column(db.Integer)
	fgMade = db.Column(db.Integer)
	ftAttempted = db.Column(db.Integer)
	ftMade = db.Column(db.Integer)
	threeAttempted = db.Column(db.Integer)
	threeMade = db.Column(db.Integer)
	PostGP = db.Column(db.Integer)
	PostGS = db.Column(db.Integer)
	PostMinutes = db.Column(db.Integer)
	PostPoints = db.Column(db.Integer)
	PostoRebounds = db.Column(db.Integer)
	PostdRebounds = db.Column(db.Integer)
	PostRebounds = db.Column(db.Integer)
	PostAssists = db.Column(db.Integer)
	PostSteals = db.Column(db.Integer)
	PostBlocks = db.Column(db.Integer)
	PostTurnovers = db.Column(db.Integer)
	PostPF = db.Column(db.Integer)
	PostfgAttempted = db.Column(db.Integer)
	PostfgMade = db.Column(db.Integer)
	PostftAttempted = db.Column(db.Integer)
	PostftMade = db.Column(db.Integer)
	PostthreeAttempted = db.Column(db.Integer)
	PostthreeMade = db.Column(db.Integer)
	note = db.Column(db.String(300))

	def serialize(self):
		return{
			"id": self.id,
			"playerID": self.playerID,
			"year": self.year,
			"stint": self.stint,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"GP": self.GP,
			"GS": self.GS,
			"minutes": self.minutes,
			"points": self.points,
			"oRebounds": self.oRebounds,
			"dRebounds": self.dRebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"PF": self.PF,
			"fgAttempted": self.fgAttempted,
			"fgMade": self.fgMade,
			"ftAttempted": self.ftAttempted,
			"ftMade": self.ftMade,
			"threeAttempted": self.threeAttempted,
			"threeMade": self.threeMade,
			"PostGP": self.PostGP,
			"PostGS": self.PostGS,
			"PostMinutes": self.PostMinutes,
			"PostPoints": self.PostPoints,
			"PostoRebounds": self.PostoRebounds,
			"PostdRebounds": self.PostdRebounds,
			"PostRebounds": self.PostRebounds,
			"PostAssists": self.PostAssists,
			"PostSteals": self.PostSteals,
			"PostBlocks": self.PostBlocks,
			"PostTurnovers": self.PostTurnovers,
			"PostPF": self.PostPF,
			"PostfgAttempted": self.PostfgAttempted,
			"PostfgMade": self.PostfgMade,
			"PostftAttempted": self.PostftAttempted,
			"PostftMade": self.PostftMade,
			"PostthreeAttempted": self.PostthreeAttempted,
			"PostthreeMade": self.PostthreeMade,
			"note": self.note,
		}
from app import db 

class players_teams(db.Model):
	__tablename__ = "players_teams"
	id = db.Column(db.Integer,unique=True,primary_key=True)
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'))
	year = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	tmID = db.Column(db.String(300),db.ForeignKey('teams.tmID'))
	lgID = db.Column(db.String(300))
	GP = db.Column(db.Integer)
	GS = db.Column(db.Integer)
	minutes = db.Column(db.Integer)
	points = db.Column(db.Integer)
	oRebounds = db.Column(db.Integer)
	dRebounds = db.Column(db.Integer)
	rebounds = db.Column(db.Integer)
	assists = db.Column(db.Integer)
	steals = db.Column(db.Integer)
	blocks = db.Column(db.Integer)
	turnovers = db.Column(db.Integer)
	PF = db.Column(db.Integer)
	fgAttempted = db.Column(db.Integer)
	fgMade = db.Column(db.Integer)
	ftAttempted = db.Column(db.Integer)
	ftMade = db.Column(db.Integer)
	threeAttempted = db.Column(db.Integer)
	threeMade = db.Column(db.Integer)
	PostGP = db.Column(db.Integer)
	PostGS = db.Column(db.Integer)
	PostMinutes = db.Column(db.Integer)
	PostPoints = db.Column(db.Integer)
	PostoRebounds = db.Column(db.Integer)
	PostdRebounds = db.Column(db.Integer)
	PostRebounds = db.Column(db.Integer)
	PostAssists = db.Column(db.Integer)
	PostSteals = db.Column(db.Integer)
	PostBlocks = db.Column(db.Integer)
	PostTurnovers = db.Column(db.Integer)
	PostPF = db.Column(db.Integer)
	PostfgAttempted = db.Column(db.Integer)
	PostfgMade = db.Column(db.Integer)
	PostftAttempted = db.Column(db.Integer)
	PostftMade = db.Column(db.Integer)
	PostthreeAttempted = db.Column(db.Integer)
	PostthreeMade = db.Column(db.Integer)
	note = db.Column(db.String(300))

	def serialize(self):
		return{
			"id": self.id,
			"playerID": self.playerID,
			"year": self.year,
			"stint": self.stint,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"GP": self.GP,
			"GS": self.GS,
			"minutes": self.minutes,
			"points": self.points,
			"oRebounds": self.oRebounds,
			"dRebounds": self.dRebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"PF": self.PF,
			"fgAttempted": self.fgAttempted,
			"fgMade": self.fgMade,
			"ftAttempted": self.ftAttempted,
			"ftMade": self.ftMade,
			"threeAttempted": self.threeAttempted,
			"threeMade": self.threeMade,
			"PostGP": self.PostGP,
			"PostGS": self.PostGS,
			"PostMinutes": self.PostMinutes,
			"PostPoints": self.PostPoints,
			"PostoRebounds": self.PostoRebounds,
			"PostdRebounds": self.PostdRebounds,
			"PostRebounds": self.PostRebounds,
			"PostAssists": self.PostAssists,
			"PostSteals": self.PostSteals,
			"PostBlocks": self.PostBlocks,
			"PostTurnovers": self.PostTurnovers,
			"PostPF": self.PostPF,
			"PostfgAttempted": self.PostfgAttempted,
			"PostfgMade": self.PostfgMade,
			"PostftAttempted": self.PostftAttempted,
			"PostftMade": self.PostftMade,
			"PostthreeAttempted": self.PostthreeAttempted,
			"PostthreeMade": self.PostthreeMade,
			"note": self.note,
		}
from app import db 

class players_teams(db.Model):
	__tablename__ = "players_teams"
	id = db.Column(db.Integer,unique=True,primary_key=True)
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'))
	year = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	tmID = db.Column(db.String(300),db.ForeignKey('teams.tmID'))
	lgID = db.Column(db.String(300))
	GP = db.Column(db.Integer)
	GS = db.Column(db.Integer)
	minutes = db.Column(db.Integer)
	points = db.Column(db.Integer)
	oRebounds = db.Column(db.Integer)
	dRebounds = db.Column(db.Integer)
	rebounds = db.Column(db.Integer)
	assists = db.Column(db.Integer)
	steals = db.Column(db.Integer)
	blocks = db.Column(db.Integer)
	turnovers = db.Column(db.Integer)
	PF = db.Column(db.Integer)
	fgAttempted = db.Column(db.Integer)
	fgMade = db.Column(db.Integer)
	ftAttempted = db.Column(db.Integer)
	ftMade = db.Column(db.Integer)
	threeAttempted = db.Column(db.Integer)
	threeMade = db.Column(db.Integer)
	PostGP = db.Column(db.Integer)
	PostGS = db.Column(db.Integer)
	PostMinutes = db.Column(db.Integer)
	PostPoints = db.Column(db.Integer)
	PostoRebounds = db.Column(db.Integer)
	PostdRebounds = db.Column(db.Integer)
	PostRebounds = db.Column(db.Integer)
	PostAssists = db.Column(db.Integer)
	PostSteals = db.Column(db.Integer)
	PostBlocks = db.Column(db.Integer)
	PostTurnovers = db.Column(db.Integer)
	PostPF = db.Column(db.Integer)
	PostfgAttempted = db.Column(db.Integer)
	PostfgMade = db.Column(db.Integer)
	PostftAttempted = db.Column(db.Integer)
	PostftMade = db.Column(db.Integer)
	PostthreeAttempted = db.Column(db.Integer)
	PostthreeMade = db.Column(db.Integer)
	note = db.Column(db.String(300))

	def serialize(self):
		return{
			"id": self.id,
			"playerID": self.playerID,
			"year": self.year,
			"stint": self.stint,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"GP": self.GP,
			"GS": self.GS,
			"minutes": self.minutes,
			"points": self.points,
			"oRebounds": self.oRebounds,
			"dRebounds": self.dRebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"PF": self.PF,
			"fgAttempted": self.fgAttempted,
			"fgMade": self.fgMade,
			"ftAttempted": self.ftAttempted,
			"ftMade": self.ftMade,
			"threeAttempted": self.threeAttempted,
			"threeMade": self.threeMade,
			"PostGP": self.PostGP,
			"PostGS": self.PostGS,
			"PostMinutes": self.PostMinutes,
			"PostPoints": self.PostPoints,
			"PostoRebounds": self.PostoRebounds,
			"PostdRebounds": self.PostdRebounds,
			"PostRebounds": self.PostRebounds,
			"PostAssists": self.PostAssists,
			"PostSteals": self.PostSteals,
			"PostBlocks": self.PostBlocks,
			"PostTurnovers": self.PostTurnovers,
			"PostPF": self.PostPF,
			"PostfgAttempted": self.PostfgAttempted,
			"PostfgMade": self.PostfgMade,
			"PostftAttempted": self.PostftAttempted,
			"PostftMade": self.PostftMade,
			"PostthreeAttempted": self.PostthreeAttempted,
			"PostthreeMade": self.PostthreeMade,
			"note": self.note,
		}
from app import db 

class players_teams(db.Model):
	__tablename__ = "players_teams"
	id = db.Column(db.Integer,unique=True,primary_key=True)
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID'))
	year = db.Column(db.Integer)
	stint = db.Column(db.Integer)
	tmID = db.Column(db.String(300),db.ForeignKey('teams.tmID'))
	lgID = db.Column(db.String(300))
	GP = db.Column(db.Integer)
	GS = db.Column(db.Integer)
	minutes = db.Column(db.Integer)
	points = db.Column(db.Integer)
	oRebounds = db.Column(db.Integer)
	dRebounds = db.Column(db.Integer)
	rebounds = db.Column(db.Integer)
	assists = db.Column(db.Integer)
	steals = db.Column(db.Integer)
	blocks = db.Column(db.Integer)
	turnovers = db.Column(db.Integer)
	PF = db.Column(db.Integer)
	fgAttempted = db.Column(db.Integer)
	fgMade = db.Column(db.Integer)
	ftAttempted = db.Column(db.Integer)
	ftMade = db.Column(db.Integer)
	threeAttempted = db.Column(db.Integer)
	threeMade = db.Column(db.Integer)
	PostGP = db.Column(db.Integer)
	PostGS = db.Column(db.Integer)
	PostMinutes = db.Column(db.Integer)
	PostPoints = db.Column(db.Integer)
	PostoRebounds = db.Column(db.Integer)
	PostdRebounds = db.Column(db.Integer)
	PostRebounds = db.Column(db.Integer)
	PostAssists = db.Column(db.Integer)
	PostSteals = db.Column(db.Integer)
	PostBlocks = db.Column(db.Integer)
	PostTurnovers = db.Column(db.Integer)
	PostPF = db.Column(db.Integer)
	PostfgAttempted = db.Column(db.Integer)
	PostfgMade = db.Column(db.Integer)
	PostftAttempted = db.Column(db.Integer)
	PostftMade = db.Column(db.Integer)
	PostthreeAttempted = db.Column(db.Integer)
	PostthreeMade = db.Column(db.Integer)
	note = db.Column(db.String(300))

	def serialize(self):
		return{
			"id": self.id,
			"playerID": self.playerID,
			"year": self.year,
			"stint": self.stint,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"GP": self.GP,
			"GS": self.GS,
			"minutes": self.minutes,
			"points": self.points,
			"oRebounds": self.oRebounds,
			"dRebounds": self.dRebounds,
			"rebounds": self.rebounds,
			"assists": self.assists,
			"steals": self.steals,
			"blocks": self.blocks,
			"turnovers": self.turnovers,
			"PF": self.PF,
			"fgAttempted": self.fgAttempted,
			"fgMade": self.fgMade,
			"ftAttempted": self.ftAttempted,
			"ftMade": self.ftMade,
			"threeAttempted": self.threeAttempted,
			"threeMade": self.threeMade,
			"PostGP": self.PostGP,
			"PostGS": self.PostGS,
			"PostMinutes": self.PostMinutes,
			"PostPoints": self.PostPoints,
			"PostoRebounds": self.PostoRebounds,
			"PostdRebounds": self.PostdRebounds,
			"PostRebounds": self.PostRebounds,
			"PostAssists": self.PostAssists,
			"PostSteals": self.PostSteals,
			"PostBlocks": self.PostBlocks,
			"PostTurnovers": self.PostTurnovers,
			"PostPF": self.PostPF,
			"PostfgAttempted": self.PostfgAttempted,
			"PostfgMade": self.PostfgMade,
			"PostftAttempted": self.PostftAttempted,
			"PostftMade": self.PostftMade,
			"PostthreeAttempted": self.PostthreeAttempted,
			"PostthreeMade": self.PostthreeMade,
			"note": self.note,
		}
