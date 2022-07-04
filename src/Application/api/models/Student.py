from app import db 

class Student(db.Model):
	__tablename__ = "Student"
	YearEnralled = db.Column(db.Integer)
	Student_ID = db.Column(db.Integer,unique=True,primary_key=True)
	GivenNames = db.Column(db.String(300))
	Program_Envollsin_program_id = db.Column(db.Integer,db.ForeignKey('Program.program_id',onupdate='CASCADE',ondelete='CASCADE'))
	Sumame = db.Column(db.String(300))

	def serialize(self):
		return{
			"YearEnralled": self.YearEnralled,
			"Student_ID": self.Student_ID,
			"GivenNames": self.GivenNames,
			"Program_Envollsin_program_id": self.Program_Envollsin_program_id,
			"Sumame": self.Sumame,
		}
