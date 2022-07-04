from app import db 

class Boaking(db.Model):
	__tablename__ = "Boaking"
	IncrementalKey = db.Column(db.Integer,unique=True,primary_key=True)
	Flight_HasBooking_IncrementalKey = db.Column(db.Integer,db.ForeignKey('Flight.IncrementalKey',onupdate='CASCADE',ondelete='CASCADE'))
	Passenger_Books_EmailAddress. = db.Column(db.String(300),db.ForeignKey('Passenger.EmailAddress.',onupdate='CASCADE',ondelete='CASCADE'))

	def serialize(self):
		return{
			"IncrementalKey": self.IncrementalKey,
			"Flight_HasBooking_IncrementalKey": self.Flight_HasBooking_IncrementalKey,
			"Passenger_Books_EmailAddress.": self.Passenger_Books_EmailAddress.,
		}
