from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
from app import db 

class teams(db.Model):
	__tablename__ = "teams"
	year = db.Column(db.Integer,primary_key=True)
	lgID = db.Column(db.String(300))
	tmID = db.Column(db.String(300),primary_key=True)
	franchID = db.Column(db.String(300))
	confID = db.Column(db.String(300))
	divID = db.Column(db.String(300))
	rank = db.Column(db.Integer)
	confRank = db.Column(db.Integer)
	playoff = db.Column(db.String(300))
	name = db.Column(db.String(300))
	draft = db.relationship('draft',backref='draft')
	series_post = db.relationship('series_post',backref='series_post')

	def serialize(self):
		return{
			"year": self.year,
			"lgID": self.lgID,
			"tmID": self.tmID,
			"franchID": self.franchID,
			"confID": self.confID,
			"divID": self.divID,
			"rank": self.rank,
			"confRank": self.confRank,
			"playoff": self.playoff,
			"name": self.name,
		}
