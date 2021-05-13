class room:
	def __init__(self, type:str, count: int):
		self.type = type
		self.count = count

	def __repr__(self):
		return f"{self.type}, count {self.count}"

	def get_type(self):
		return self.type

	def reserve(self):
		pass



a1 = room("single", 10)
print(a1)