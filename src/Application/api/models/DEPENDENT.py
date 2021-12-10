from app import db 

class DEPENDENT(db.Model):
	__tablename__ = "DEPENDENT"
	sex = db.Column(db.String(300))
	relatlonship = db.Column(db.String(300))
	name = db.Column(db.String(300))
	birth_date = db.Column(db.DateTime)
	Dependents_EMPLOYEE_ = db.Column(db.String(300),db.ForeignKey('EMPLOYEE.ssn'),primary_key=True)

	def serialize(self):
		return{
			"sex": self.sex,
			"relatlonship": self.relatlonship,
			"name": self.name,
			"birth_date": self.birth_date,
			"Dependents_EMPLOYEE_": self.Dependents_EMPLOYEE_,
		}
