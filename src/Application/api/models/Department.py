from app import db 

class Department(db.Model):
	__tablename__ = "Department"
	description = db.Column(db.String(300))
	name = db.Column(db.String(300),unique=True,primary_key=True)

	def serialize(self):
		return{
			"description": self.description,
			"name": self.name,
		}
