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

	def get_course():
		return self.course

	def get_faculty():
		return self.faculty

	def get_university():
		return self.university

	def __repr__(self):
		super().__repr__(name, surname, age, gender)
		return f"{self.name.title()} {self.surname.title()} - {self.gender.title()}, {self.age} years old, studies in {self.university}"



p_1 = Person("Steve", "Wonder", 26, "Male")
#print(p_1)

s_1 = Student("Steve", "Wonder", 26, "Male", "ASUE", "Management", 2, 9)
print(s_1)