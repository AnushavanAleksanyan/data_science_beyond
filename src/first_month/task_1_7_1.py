from task_1_5_2 import Money


class Person():
	gend=("Male", "Female")
	def __init__(self, name: str, surname: str, age: int, gender: str):
		self.__name = name
		self.__surname = surname
		self.__age = age
		if not gender.title() in self.gend:
			print("person's gender should be 'male' or 'female'")
			raise SyntaxError
		self.__gender = gender

	def __repr__(self):
		return f"{self.__name.title()} {self.__surname.title()} - {self.__gender.title()}, {self.__age} years old"


class Student(Person):
	def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, course:int, middle_score: int):
		super().__init__(name, surname, age, gender)
		self.__university = university
		self.__faculty = faculty
		self.__course = course
		self.__middle_score = middle_score

	def __repr__(self):
		return f"{super().__repr__()}, studies in {self.__university}"

	def get_score(self):
		return self.__middle_score

	def set_score(self, score):
		if isinstance(score, int):
			self.__middle_score = score

	def get_course(self):
		return self.__course

	def set_course(self, course):
		if isinstance(course, int):
			self.__course = course

	def get_faculty(self):
		return self.__faculty

	def set_faculty(self, faculty):
		if isinstance(faculty, str):
			self.__faculty = faculty

	def get_university(self):
		return self.__university

	def set_university(self, university):
		if isinstance(university, str):
			self.__university = university

class Teacher(Person):
	def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, discipline: int, experience: int, salery: Money):
		super().__init__(name, surname, age, gender)
		self.__university = university
		self.__faculty = faculty
		self.__discipline = discipline
		self.__experience = experience
		self.__salery = Money(salery, "USD").change("AMD")

	def get_discipline(self):
		return self.__discipline

	def set_discipline(self, discipline):
		if isinstance(discipline, int):
			self.__discipline = discipline

	def get_faculty(self):
		return self.__faculty

	def set_faculty(self, faculty):
		if isinstance(faculty, str):
			self.__faculty = faculty

	def get_university(self):
		return self.__university

	def set_university(self, university):
		if isinstance(university, str):
			self.__university = university

	def get_experience(self):
		return self.__experience

	def set_experience(self, experience):
		if isinstance(experience, int):
			self.__experience = experience

	def get_salery(self):
		return self.__salery

	def set_salery(self, salery):
		if isinstance(salery, int):
			self.__salery = Money(salery, "USD").change("AMD")

	def __repr__(self):
		return f"{super().__repr__()}, experience: {self.__experience}, salery is {self.__salery}"



p_1 = Person("Steve", "Wonder", 26, "Male")
#print(p_1)

s_1 = Student("Steve", "Wonder", 26, "Male", "ASUE", "Management", 2, 9)
# print(s_1.get_university())
# s_1.set_university(10)
# print(s_1.get_university())
# print(s_1)

t_1 = Teacher("Barry", "White", 31, "Male", "ASUE", "Management", "Municipal management", "5", 1000)
print(t_1.get_salery())
t_1.set_salery(1200)
print(t_1.get_salery())
print(t_1)