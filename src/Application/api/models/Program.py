from app import db 

class Program(db.Model):
	__tablename__ = "Program"
	YearCommenced = db.Column(db.Integer)
	program_id = db.Column(db.Integer,unique=True,primary_key=True)
	Name = db.Column(db.String(300))
	CreditPoints = db.Column(db.Float)

	def serialize(self):
		return{
			"YearCommenced": self.YearCommenced,
			"program_id": self.program_id,
			"Name": self.Name,
			"CreditPoints": self.CreditPoints,
		}
