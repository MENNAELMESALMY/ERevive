from app import db 

class Works_EMPLOYEE_PROJECT(db.Model):
	__tablename__ = "Works_EMPLOYEE_PROJECT"
	start_date = db.Column(db.DateTime)
	hours = db.Column(db.Integer)
	EMPLOYEE_ = db.Column(db.String(300),db.ForeignKey('EMPLOYEE.ssn'),primary_key=True)
	PROJECT_ = db.Column(db.String(300),db.ForeignKey('PROJECT.name'),primary_key=True)

	def serialize(self):
		return{
			"start_date": self.start_date,
			"hours": self.hours,
			"EMPLOYEE_": self.EMPLOYEE_,
			"PROJECT_": self.PROJECT_,
		}
