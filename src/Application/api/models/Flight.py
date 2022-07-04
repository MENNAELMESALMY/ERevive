from app import db 

class Flight(db.Model):
	__tablename__ = "Flight"
	ArrivalDate = db.Column(db.DateTime)
	Departureime = db.Column(db.String(300))
	DepartureDate = db.Column(db.DateTime)
	to = db.Column(db.String(300))
	From = db.Column(db.String(300))
	FlightNumber = db.Column(db.Integer)
	IncrementalKey = db.Column(db.Integer,unique=True,primary_key=True)
	Airplane_Flies_IncrementalKey = db.Column(db.Integer,db.ForeignKey('Airplane.IncrementalKey',onupdate='CASCADE',ondelete='CASCADE'))

	def serialize(self):
		return{
			"ArrivalDate": self.ArrivalDate,
			"Departureime": self.Departureime,
			"DepartureDate": self.DepartureDate,
			"to": self.to,
			"From": self.From,
			"FlightNumber": self.FlightNumber,
			"IncrementalKey": self.IncrementalKey,
			"Airplane_Flies_IncrementalKey": self.Airplane_Flies_IncrementalKey,
		}
