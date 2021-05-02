from task_1_5_2 import Money


class Person():
	gender=("Male", "Female")
	def __init__(self, name: str, surname: str, age: int, gender: str):
		self.name = name
		self.surname = surname
		self.age = age
		if not gender.title() in self.gender:
			print("person's gender should be 'male' or 'female'")
			raise SyntaxError
		self.gender = gender

	def __repr__(self):
		return f"{self.name.title()} {self.surname.title()} - {self.gender.title()}, {self.age} years old"


class Student(Person):
	def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, course:int, middle_score: int):
		super().__init__(name, surname, age, gender)
		self.university = university
		self.faculty = faculty
		self.course = course
		self.middle_score = middle_score

	def get_score(self):
		return self.middle_score

	def get_course(self):
		return self.course

	def get_faculty(self):
		return self.faculty

	def get_university(self):
		return self.university

	def __repr__(self):
		return f"{self.name.title()} {self.surname.title()} - {self.gender.title()}, {self.age} years old, studies in {self.university}"


class Teacher(Person):
	def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, discipline: int, experience: int, salery: Money):
		super().__init__(name, surname, age, gender)
		self.university = university
		self.faculty = faculty
		self.discipline = discipline
		self.experience = experience
		self.salery = salery

	def get_discipline(self):
		return self.discipline

	def get_faculty(self):
		return self.faculty

	def get_university(self):
		return self.university

	def get_experience(self):
		return self.experience

	def get_salary(self):
		return self.salery

	def __repr__(self):
		return f"{self.name.title()} {self.surname.title()} - {self.gender.title()}, {self.age} years old, experience: {self.experience}, salery is {self.salery}"



p_1 = Person("Steve", "Wonder", 26, "Male")
#print(p_1)

s_1 = Student("Steve", "Wonder", 26, "Male", "ASUE", "Management", 2, 9)
#print(s_1.get_faculty())

salery = Money(1000, "USD").change("AMD")

t_1 = Teacher("Barry", "White", 31, "Male", "ASUE", "Management", "Municipal management", "5", 1000)
print(t_1)