from app import db 

class Login(db.Model):
	__tablename__ = "Login"
	password = db.Column(db.String(300))
	username = db.Column(db.String(300),unique=True,primary_key=True)

	def serialize(self):
		return{
			"password": self.password,
			"username": self.username,
		}
