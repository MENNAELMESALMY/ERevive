from app import db 

class PROJECT(db.Model):
	__tablename__ = "PROJECT"
	location = db.Column(db.String(300))
	name = db.Column(db.String(300),primary_key=True)
	budget = db.Column(db.Float)
	DEPARTMENT_Assigned_name = db.Column(db.String(300),db.ForeignKey('DEPARTMENT.name'))

	def serialize(self):
		return{
			"location": self.location,
			"name": self.name,
			"budget": self.budget,
			"DEPARTMENT_Assigned_name": self.DEPARTMENT_Assigned_name,
		}
