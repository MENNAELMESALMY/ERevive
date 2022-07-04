from app import db 

class Passenger(db.Model):
	__tablename__ = "Passenger"
	‘Surname = db.Column(db.String(300))
	GivenNames = db.Column(db.String(300))
	EmailAddress. = db.Column(db.String(300),unique=True,primary_key=True)

	def serialize(self):
		return{
			"‘Surname": self.‘Surname,
			"GivenNames": self.GivenNames,
			"EmailAddress.": self.EmailAddress.,
		}
