from app import db 

class course(db.Model):
	__tablename__ = "course"
	YearCommenced = db.Column(db.Integer)
	course_id = db.Column(db.Integer,unique=True,primary_key=True)
	Name = db.Column(db.String(300))
	CreditPoints = db.Column(db.Float)
	contains_Program_program_id = db.Column(db.Integer,db.ForeignKey('Program.program_id',onupdate='CASCADE',ondelete='CASCADE'),unique=True,primary_key=True)

	def serialize(self):
		return{
			"YearCommenced": self.YearCommenced,
			"course_id": self.course_id,
			"Name": self.Name,
			"CreditPoints": self.CreditPoints,
			"contains_Program_program_id": self.contains_Program_program_id,
		}
