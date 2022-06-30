from app import db 

class awards_coaches(db.Model):
	__tablename__ = "awards_coaches"
	id = db.Column(db.String(300),unique=True,primary_key=True)
	coachID = db.Column(db.String(300),db.ForeignKey('coaches.coachID',onupdate='CASCADE',ondelete='CASCADE'))
	award = db.Column(db.String(300))
	lgID = db.Column(db.String(300))
	note = db.Column(db.String(300))

	def serialize(self):
		return{
			"id": self.id,
			"coachID": self.coachID,
			"award": self.award,
			"lgID": self.lgID,
			"note": self.note,
		}
