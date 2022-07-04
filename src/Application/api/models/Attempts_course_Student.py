from app import db 

class Attempts_course_Student(db.Model):
	__tablename__ = "Attempts_course_Student"
	Year = db.Column(db.Integer)
	Grade = db.Column(db.String(300))
	Mark = db.Column(db.String(300))
	Semester = db.Column(db.String(300))
	Student_Student_ID = db.Column(db.Integer,db.ForeignKey('Student.Student_ID',onupdate='CASCADE',ondelete='CASCADE'),unique=True,primary_key=True)
	course_Program_program_id = db.Column(db.Integer,db.ForeignKey('course.contains_Program_program_id',onupdate='CASCADE',ondelete='CASCADE'),unique=True,primary_key=True)
	course_course_id = db.Column(db.Integer,db.ForeignKey('course.course_id',onupdate='CASCADE',ondelete='CASCADE'),unique=True,primary_key=True)

	def serialize(self):
		return{
			"Year": self.Year,
			"Grade": self.Grade,
			"Mark": self.Mark,
			"Semester": self.Semester,
			"Student_Student_ID": self.Student_Student_ID,
			"course_Program_program_id": self.course_Program_program_id,
			"course_course_id": self.course_course_id,
		}
