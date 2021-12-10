from app import db 

class EMPLOYEE(db.Model):
	__tablename__ = "EMPLOYEE"
	last_name = db.Column(db.String(300))
	middle_initis = db.Column(db.String(300))
	first_name = db.Column(db.String(300))
	address = db.Column(db.String(300))
	salary = db.Column(db.Float)
	sex = db.Column(db.String(300))
	status = db.Column(db.String(300))
	birth_dat = db.Column(db.String(300))
	ssn = db.Column(db.String(300),primary_key=True)
	start_date = db.Column(db.DateTime)
	DEPARTMENT_Employed_name = db.Column(db.String(300),db.ForeignKey('DEPARTMENT.name'))
	EMPLOYEE_Supervision_ = db.Column(db.String(300),db.ForeignKey('EMPLOYEE.ssn'))
	DEPARTMENT = db.relationship('DEPARTMENT',backref='DEPARTMENT')
	DEPENDENT = db.relationship('DEPENDENT',backref='DEPENDENT')
	PROJECT = db.relationship('PROJECT',secondary='Works_EMPLOYEE_PROJECT',backref=db.backref('PROJECT',lazy='dynamic'))

	def serialize(self):
		return{
			"last_name": self.last_name,
			"middle_initis": self.middle_initis,
			"first_name": self.first_name,
			"address": self.address,
			"salary": self.salary,
			"sex": self.sex,
			"status": self.status,
			"birth_dat": self.birth_dat,
			"ssn": self.ssn,
			"start_date": self.start_date,
			"DEPARTMENT_Employed_name": self.DEPARTMENT_Employed_name,
			"EMPLOYEE_Supervision_": self.EMPLOYEE_Supervision_,
		}
