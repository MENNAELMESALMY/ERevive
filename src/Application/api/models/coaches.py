from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
from app import db 

class coaches(db.Model):
	__tablename__ = "coaches"
	coachID = db.Column(db.String(300),primary_key=True)
	year = db.Column(db.Integer,primary_key=True)
	tmID = db.Column(db.String(300),primary_key=True)
	lgID = db.Column(db.String(300))
	stint = db.Column(db.Integer,primary_key=True)
	won = db.Column(db.Integer)
	lost = db.Column(db.Integer)
	post_wins = db.Column(db.Integer)
	post_losses = db.Column(db.Integer)
	awards_coaches = db.relationship('awards_coaches',backref='awards_coaches')

	def serialize(self):
		return{
			"coachID": self.coachID,
			"year": self.year,
			"tmID": self.tmID,
			"lgID": self.lgID,
			"stint": self.stint,
			"won": self.won,
			"lost": self.lost,
			"post_wins": self.post_wins,
			"post_losses": self.post_losses,
		}
