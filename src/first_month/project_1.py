class Room:
	reserved = False
	room_number = 0
	count = {"single":0, "double": 0, "penthouse":0}

	def __init__(self, type:str):
		self.__type = type
		Room.count[self.__type] += 1

	def __repr__(self):
		return f"{self.__type}, {self.reserved}"

	def get_type(self):
		return self.__type

	def get_count(self):
		return f"Free {self.count[self.__type]} '{self.__type}' rooms"

	def reserve(self):
		if not self.reserved:
			self.reserved = True
			Room.count[self.__type] -= 1

	def checkout(self):
		if self.reserved:
			self.reserved = False
			Room.count[self.__type] += 1


class Hotel(Room):
	rating = 0
	rater_count = 0
	rooms = []

	def __init__(self, name):
		super().__init__(type)
		self.name = name

	def rate(self, mark):
		self.rater_count +=1
		self.rating = (self.rating + mark)//self.rater_count

	def get_rating(self):
		return self.rating

	def add_room(self, room):
		self.rooms.append(room)

	def remove_room(self, room):
		self.rooms.remove(room)

	def get_rooms(self):
		return self.rooms

	def reserve(self):
		pass

	def checkout(self):
		pass


r1 = Room("single")
print(r1)
r1.reserve()
print(r1.get_count())
print(r1)
#print(r1.get_type())
r1.checkout()
#print(r1)
print(r1.get_count())

r2 = Room("double")
# r2.reserve()
# print(r2)
print(r2.get_count())


# r3 = Room("double")
# r3.reserve()
# print(r3.get_count())
print("*************")


# h1 = Hotel("MyHotel")
# h1.add_room(r1)
# h1.add_room(r2)
# print(h1.get_rooms())

# h1.rate(10)
# h1.rate(3)
# h1.rate(10)
# print(h1.get_rating())