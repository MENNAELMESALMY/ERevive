from app import db 

class DEPARTMENT_Clocation(db.Model):
	__tablename__ = "DEPARTMENT_Clocation"
	Clocation = db.Column(db.String(300),primary_key=True)
	DEPARTMENT_name = db.Column(db.String(300),db.ForeignKey('DEPARTMENT.name'),primary_key=True)

	def serialize(self):
		return{
			"Clocation": self.Clocation,
			"DEPARTMENT_name": self.DEPARTMENT_name,
		}
