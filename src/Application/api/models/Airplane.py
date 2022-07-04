from app import db 

class Airplane(db.Model):
	__tablename__ = "Airplane"
	RegistrationNumnber = db.Column(db.String(300))
	MadelNumber = db.Column(db.Integer)
	Capacity = db.Column(db.Integer)
	IncrementalKey = db.Column(db.Integer,unique=True,primary_key=True)

	def serialize(self):
		return{
			"RegistrationNumnber": self.RegistrationNumnber,
			"MadelNumber": self.MadelNumber,
			"Capacity": self.Capacity,
			"IncrementalKey": self.IncrementalKey,
		}
