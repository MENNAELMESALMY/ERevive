from app import db 

class Role(db.Model):
	__tablename__ = "Role"
	description = db.Column(db.String(300))
	name = db.Column(db.String(300),unique=True,primary_key=True)

	def serialize(self):
		return{
			"description": self.description,
			"name": self.name,
		}
