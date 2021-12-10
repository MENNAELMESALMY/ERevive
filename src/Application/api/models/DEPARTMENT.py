from app import db 

class DEPARTMENT(db.Model):
	__tablename__ = "DEPARTMENT"
	name = db.Column(db.String(300),primary_key=True)
	start_date = db.Column(db.DateTime)
	EMPLOYEE_Manages = db.Column(db.String(300),db.ForeignKey('EMPLOYEE.ssn'))
	DEPARTMENT_Clocation = db.relationship('DEPARTMENT_Clocation',backref='DEPARTMENT_Clocation')
	EMPLOYEE = db.relationship('EMPLOYEE',backref='EMPLOYEE')
	PROJECT = db.relationship('PROJECT',backref='PROJECT')

	def serialize(self):
		return{
			"name": self.name,
			"start_date": self.start_date,
			"EMPLOYEE_Manages": self.EMPLOYEE_Manages,
		}
