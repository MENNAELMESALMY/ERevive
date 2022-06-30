from app import db 

class awards_players(db.Model):
	__tablename__ = "awards_players"
	playerID = db.Column(db.String(300),db.ForeignKey('players.playerID',onupdate='CASCADE',ondelete='CASCADE'))
	award = db.Column(db.String(300))
	year = db.Column(db.Integer,unique=True,primary_key=True)
	lgID = db.Column(db.String(300),unique=True,primary_key=True)
	note = db.Column(db.String(300))
	pos = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"award": self.award,
			"year": self.year,
			"lgID": self.lgID,
			"note": self.note,
			"pos": self.pos,
		}