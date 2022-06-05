from app import db 

class players(db.Model):
	__tablename__ = "players"
	playerID = db.Column(db.String(300),unique=True,primary_key=True)
	useFirst = db.Column(db.String(300))
	firstName = db.Column(db.String(300))
	middleName = db.Column(db.String(300))
	lastName = db.Column(db.String(300))
	nameGiven = db.Column(db.String(300))
	fullGivenName = db.Column(db.String(300))
	nameSuffix = db.Column(db.String(300))
	nameNick = db.Column(db.String(300))
	pos = db.Column(db.String(300))
	firstseason = db.Column(db.Integer)
	lastseason = db.Column(db.Integer)
	height = db.Column(db.Float)
	weight = db.Column(db.Integer)
	college = db.Column(db.String(300))
	collegeOther = db.Column(db.String(300))
	birthDate = db.Column(db.DateTime)
	birthCity = db.Column(db.String(300))
	birthState = db.Column(db.String(300))
	birthCountry = db.Column(db.String(300))
	highSchool = db.Column(db.String(300))
	hsCity = db.Column(db.String(300))
	hsState = db.Column(db.String(300))
	hsCountry = db.Column(db.String(300))
	deathDate = db.Column(db.DateTime)
	race = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"useFirst": self.useFirst,
			"firstName": self.firstName,
			"middleName": self.middleName,
			"lastName": self.lastName,
			"nameGiven": self.nameGiven,
			"fullGivenName": self.fullGivenName,
			"nameSuffix": self.nameSuffix,
			"nameNick": self.nameNick,
			"pos": self.pos,
			"firstseason": self.firstseason,
			"lastseason": self.lastseason,
			"height": self.height,
			"weight": self.weight,
			"college": self.college,
			"collegeOther": self.collegeOther,
			"birthDate": self.birthDate,
			"birthCity": self.birthCity,
			"birthState": self.birthState,
			"birthCountry": self.birthCountry,
			"highSchool": self.highSchool,
			"hsCity": self.hsCity,
			"hsState": self.hsState,
			"hsCountry": self.hsCountry,
			"deathDate": self.deathDate,
			"race": self.race,
		}
from app import db 

class players(db.Model):
	__tablename__ = "players"
	playerID = db.Column(db.String(300),unique=True,primary_key=True)
	useFirst = db.Column(db.String(300))
	firstName = db.Column(db.String(300))
	middleName = db.Column(db.String(300))
	lastName = db.Column(db.String(300))
	nameGiven = db.Column(db.String(300))
	fullGivenName = db.Column(db.String(300))
	nameSuffix = db.Column(db.String(300))
	nameNick = db.Column(db.String(300))
	pos = db.Column(db.String(300))
	firstseason = db.Column(db.Integer)
	lastseason = db.Column(db.Integer)
	height = db.Column(db.Float)
	weight = db.Column(db.Integer)
	college = db.Column(db.String(300))
	collegeOther = db.Column(db.String(300))
	birthDate = db.Column(db.DateTime)
	birthCity = db.Column(db.String(300))
	birthState = db.Column(db.String(300))
	birthCountry = db.Column(db.String(300))
	highSchool = db.Column(db.String(300))
	hsCity = db.Column(db.String(300))
	hsState = db.Column(db.String(300))
	hsCountry = db.Column(db.String(300))
	deathDate = db.Column(db.DateTime)
	race = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"useFirst": self.useFirst,
			"firstName": self.firstName,
			"middleName": self.middleName,
			"lastName": self.lastName,
			"nameGiven": self.nameGiven,
			"fullGivenName": self.fullGivenName,
			"nameSuffix": self.nameSuffix,
			"nameNick": self.nameNick,
			"pos": self.pos,
			"firstseason": self.firstseason,
			"lastseason": self.lastseason,
			"height": self.height,
			"weight": self.weight,
			"college": self.college,
			"collegeOther": self.collegeOther,
			"birthDate": self.birthDate,
			"birthCity": self.birthCity,
			"birthState": self.birthState,
			"birthCountry": self.birthCountry,
			"highSchool": self.highSchool,
			"hsCity": self.hsCity,
			"hsState": self.hsState,
			"hsCountry": self.hsCountry,
			"deathDate": self.deathDate,
			"race": self.race,
		}
from app import db 

class players(db.Model):
	__tablename__ = "players"
	playerID = db.Column(db.String(300),unique=True,primary_key=True)
	useFirst = db.Column(db.String(300))
	firstName = db.Column(db.String(300))
	middleName = db.Column(db.String(300))
	lastName = db.Column(db.String(300))
	nameGiven = db.Column(db.String(300))
	fullGivenName = db.Column(db.String(300))
	nameSuffix = db.Column(db.String(300))
	nameNick = db.Column(db.String(300))
	pos = db.Column(db.String(300))
	firstseason = db.Column(db.Integer)
	lastseason = db.Column(db.Integer)
	height = db.Column(db.Float)
	weight = db.Column(db.Integer)
	college = db.Column(db.String(300))
	collegeOther = db.Column(db.String(300))
	birthDate = db.Column(db.DateTime)
	birthCity = db.Column(db.String(300))
	birthState = db.Column(db.String(300))
	birthCountry = db.Column(db.String(300))
	highSchool = db.Column(db.String(300))
	hsCity = db.Column(db.String(300))
	hsState = db.Column(db.String(300))
	hsCountry = db.Column(db.String(300))
	deathDate = db.Column(db.DateTime)
	race = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"useFirst": self.useFirst,
			"firstName": self.firstName,
			"middleName": self.middleName,
			"lastName": self.lastName,
			"nameGiven": self.nameGiven,
			"fullGivenName": self.fullGivenName,
			"nameSuffix": self.nameSuffix,
			"nameNick": self.nameNick,
			"pos": self.pos,
			"firstseason": self.firstseason,
			"lastseason": self.lastseason,
			"height": self.height,
			"weight": self.weight,
			"college": self.college,
			"collegeOther": self.collegeOther,
			"birthDate": self.birthDate,
			"birthCity": self.birthCity,
			"birthState": self.birthState,
			"birthCountry": self.birthCountry,
			"highSchool": self.highSchool,
			"hsCity": self.hsCity,
			"hsState": self.hsState,
			"hsCountry": self.hsCountry,
			"deathDate": self.deathDate,
			"race": self.race,
		}
from app import db 

class players(db.Model):
	__tablename__ = "players"
	playerID = db.Column(db.String(300),unique=True,primary_key=True)
	useFirst = db.Column(db.String(300))
	firstName = db.Column(db.String(300))
	middleName = db.Column(db.String(300))
	lastName = db.Column(db.String(300))
	nameGiven = db.Column(db.String(300))
	fullGivenName = db.Column(db.String(300))
	nameSuffix = db.Column(db.String(300))
	nameNick = db.Column(db.String(300))
	pos = db.Column(db.String(300))
	firstseason = db.Column(db.Integer)
	lastseason = db.Column(db.Integer)
	height = db.Column(db.Float)
	weight = db.Column(db.Integer)
	college = db.Column(db.String(300))
	collegeOther = db.Column(db.String(300))
	birthDate = db.Column(db.DateTime)
	birthCity = db.Column(db.String(300))
	birthState = db.Column(db.String(300))
	birthCountry = db.Column(db.String(300))
	highSchool = db.Column(db.String(300))
	hsCity = db.Column(db.String(300))
	hsState = db.Column(db.String(300))
	hsCountry = db.Column(db.String(300))
	deathDate = db.Column(db.DateTime)
	race = db.Column(db.String(300))

	def serialize(self):
		return{
			"playerID": self.playerID,
			"useFirst": self.useFirst,
			"firstName": self.firstName,
			"middleName": self.middleName,
			"lastName": self.lastName,
			"nameGiven": self.nameGiven,
			"fullGivenName": self.fullGivenName,
			"nameSuffix": self.nameSuffix,
			"nameNick": self.nameNick,
			"pos": self.pos,
			"firstseason": self.firstseason,
			"lastseason": self.lastseason,
			"height": self.height,
			"weight": self.weight,
			"college": self.college,
			"collegeOther": self.collegeOther,
			"birthDate": self.birthDate,
			"birthCity": self.birthCity,
			"birthState": self.birthState,
			"birthCountry": self.birthCountry,
			"highSchool": self.highSchool,
			"hsCity": self.hsCity,
			"hsState": self.hsState,
			"hsCountry": self.hsCountry,
			"deathDate": self.deathDate,
			"race": self.race,
		}
