class Room:
	reserved = False
	room_number = 0
	count = 0

	def __init__(self, type:str):
		self.type = type

	def __repr__(self):
		return f"{self.type}, {self.reserved}"

	def get_type(self):
		return self.type

	def get_count(self):
		return self.count

	def reserve(self):
		self.reserved = True
		Room.count += 1

	def checkout(self):
		self.reserved = False
		Room.count -= 1


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
print(r1.get_type())
#r1.checkout()
print(r1)
print(r1.get_count())

r2 = Room("double")
r2.reserve()
print(r2)
print(r2.get_count())


r3 = Room("double")
print("*************")


h1 = Hotel("MyHotel")
h1.add_room(r1)
h1.add_room(r2)
print(h1.get_rooms())
# h1.rate(10)
# h1.rate(3)
# h1.rate(10)
# print(h1.get_rating())