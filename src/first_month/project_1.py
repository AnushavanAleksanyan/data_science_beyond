class Room:
	def __init__(self, type:str, count):
		self.__type = type
		self.__count = count

	def __repr__(self):
		return f"{self.__type}, {self.__count}"

	def get_type(self):
		return self.__type

	def get_count(self):
		return self.__count

	def reserve(self, type, count):
		if count<=self.__count:
			self.__count -= count
		else:
			print(f"You can only reserve {self.__count} rooms")
		return Room(self.__type, self.__count)

	def checkout(self, type, count):
		self.__count += count


class Hotel(Room):
	def __init__(self, name):
		self.__name = name
		self.__rating = 0
		self.__rater_count = 0
		self.__rooms = []

	def __repr__(self):
		return f"{self.__name} \nrating - {self.__rating} \nrated {self.__rater_count} people, "

	def rate(self, mark):
		self.__rater_count +=1
		self.__rating = (self.__rating + mark)//self.__rater_count

	def get_rating(self):
		return self.__rating

	def add_room(self, room):
		self.__rooms.append(room)

	def remove_room(self, room):
		self.__rooms.remove(room)

	def get_rooms(self):
		qntty = self.__rooms[0].get_count()
		return self.__rooms, qntty

	# def reserve(self):
	# 	super().reserve()

	# def checkout(self):
	# 	pass


r1 = Room("single", 5)
print(r1)
print(r1.get_type())
# r1.reserve("single", 2)
# print(r1.get_count())
# r1.checkout("single", 1)
# print(r1)
#print(r1.get_count())

r2 = Room("double", 8)
# r2.reserve()
print(r2)
print(r2.get_count())


# r3 = Room("penthouse", 4)
# r3.reserve()
# print(r3.get_count())
print("*************")


h1 = Hotel("MyHotel")
h1.add_room(r1)
h1.add_room(r2)
# h1.add_room(r3)
print(h1.get_rooms())
# h1.rate(10)
# h1.rate(3)
# print(h1.get_rating())

# print(r1.get_count())
# h1.reserve("single", 2)
# print(r1.get_count())
#print(h1.get_count())

#print(h1)