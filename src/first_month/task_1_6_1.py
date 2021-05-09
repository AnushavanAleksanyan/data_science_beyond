class RationalClassError(Exception):
	def __init__(self, err_text, val):
		self.err_text = err_text
		self.val = val
	def print_obj(self):
		print(self.err_text, "|", self.val)


class Rational:
	def __init__(self, numerator, denumerator):
		try:
			if not isinstance(numerator, int):
				raise RationalClassError("wrong numerator type", numerator)
			elif not isinstance(denumerator, int):
				raise RationalClassError("wrong denumerator type", denumerator)
		except RationalClassError as mte:
			mte.print_obj()
		else:
			try:
				if denumerator==0:
					raise RationalClassError("Can't devide to zero", denumerator)
			except RationalClassError as ze:
				ze.print_obj()
			else:
				self.__numerator = self.normalize(numerator, numerator, denumerator)
				self.__denumerator = self.normalize(denumerator, numerator, denumerator)

	@staticmethod
	def gcd(a, b):
		while a > 0 and b > 0:
			if a > b:
				a = a % b
			else:
				b = b % a
		return a+b

	@staticmethod
	def normalize(num, numer, denumer):
		return num//Rational.gcd(numer,denumer)

	def __repr__(self):
		return str(self.__numerator) +" / "+ str(self.__denumerator)

	def get_elems(self):
		return self.__numerator, self.__denumerator

	def set_elems(self, x,y):
		try:
			if type(x) != int:
				raise RationalClassError("wrong numerator type", x)
			elif type(y) != int:
				raise RationalClassError("wrong denumerator type", y)
		except RationalClassError as mte:
			mte.print_obj()
		else:
			self.__numerator = x
			self.__denumerator = y

	def del_elems(self):
		del self.__numerator
		del self.__denumerator

	elems = property(get_elems, set_elems, del_elems, doc = "property for numerator")

	def	__add__(self, other):
		x = self.__numerator * other.__denumerator+self.__denumerator*other.__numerator
		y = self.__denumerator*other.__denumerator
		return Rational(x,y)

	def	__sub__(self, other):
		x = self.__numerator * other.__denumerator-self.__denumerator*other.__numerator
		y = self.__denumerator*other.__denumerator
		return Rational(x,y)

	def	__mul__(self, other):
		x = self.__numerator * other.__numerator
		y = self.__denumerator * other.__denumerator
		return Rational(x,y)

	def	__truediv__(self, other):
		x = self.__numerator / other.__denumerator
		y = self.__denumerator / other.__numerator
		return Rational(x,y)

	def	__eq__(self, other):

		if self.__numerator * other.__denumerator == self.__denumerator * other.__numerator:
			return True
		else:
			return False

	def	__gt__(self, other):
		if self.__numerator*other.__denumerator>self.__denumerator*other.__numerator:
			return True
		else:
			return False

	def	__ge__(self, other):
		if self.__numerator*other.__denumerator>=self.__denumerator*other.__numerator:
			return True
		else:
			return False

	def	__lt__(self, other):
		if self.__numerator*other.__denumerator<self.__denumerator*other.__numerator:
			return True
		else:
			return False

	def	__le__(self, other):
		if self.__numerator*other.__denumerator<=self.__denumerator*other.__numerator:
			return True
		else:
			return False

	def __pow__(self, num):
		try:
			if type(num) != int:
				raise RationalClassError("wrong multiplicator type", num)
		except RationalClassError as rce:
			rce.print_obj()
		else:
			x = self.__numerator**int(num)
			y = self.__denumerator**int(num)
			return Rational(x,y)


a = Rational(5,8)
b = Rational(1,4)

print(a)
print(a.elems)
a.elems = 6,3
print(a.elems)
print(a**"2")