# Create a reservation system which books  hotel rooms.
# It charges various rates for particular sections of the hotel
class Room:
	def __init__(self, type, count):
		self.__type = type
		self.__count = count    # free rooms

	def __repr__(self):
		return f"{self.__count} {self.__type} rooms"

	def get_type(self):
		return self.__type

	def get_count(self):
		return self.__count

	def reserve(self, count):
		if count <= self.__count:
			self.__count -= count
		else:
			print(f"We have only {self.__count} free {self.__type} rooms")

	def checkout(self):
		self.__count += count



class Hotel:
	def __init__(self):
		self.__name = ""
		self.__rating = 0
		self.__rater_count = 0
		self.__rooms = []

	def __repr__(self):
		return self.__name

	def get_rating(self):
		return self.__rating

	def get_rooms(self):
		return self.__rooms

	def reserve(self, room, count):
		if room in self.__rooms:
			room.reserve(count)
		else:
			print("We don't have such room")

	def checkout(self):
		if room in self.__rooms:
			room.checkout(count)
		else:
			print("We don't have such room")

	def rate(self, mark):
		self.__rater_count += 1
		self.__rating = (self.__rating + mark)/self.__rater_count

	def add_room(self, room):
		self.__rooms.append(room)

	def remove_room(self, room):
		self.__rooms.remove(room)

# code samples
r1 = Room("Single", 10)
r1.reserve(13)
print(r1)
r2 = Room("Double", 15)


h1 = Hotel()
h1.name = "Malibu"
h1.rate(10)
h1.rate(8)
print(h1)
h1.add_room(r1)
h1.add_room(r2)
print(h1.get_rooms())
h1.reserve(r1, 2)
print(h1.get_rating())