from app import db 

class Employee(db.Model):
	__tablename__ = "Employee"
	name = db.Column(db.String(300))
	phone = db.Column(db.String(300))
	email = db.Column(db.String(300),unique=True,primary_key=True)
	Login_Has_username = db.Column(db.String(300),db.ForeignKey('Login.username',onupdate='CASCADE',ondelete='CASCADE'))
	Role_Has_name = db.Column(db.String(300),db.ForeignKey('Role.name',onupdate='CASCADE',ondelete='CASCADE'))
	Department_Has_name = db.Column(db.String(300),db.ForeignKey('Department.name',onupdate='CASCADE',ondelete='CASCADE'))

	def serialize(self):
		return{
			"name": self.name,
			"phone": self.phone,
			"email": self.email,
			"Login_Has_username": self.Login_Has_username,
			"Role_Has_name": self.Role_Has_name,
			"Department_Has_name": self.Department_Has_name,
		}
