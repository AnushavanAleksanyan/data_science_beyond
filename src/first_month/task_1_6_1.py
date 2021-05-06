class ZeroError(Exception):
	def __init__(self, err_text):
		self.err_text = err_text
	def print_obj(self):
		print(self.err_text)

class MyTypeError(Exception):
	def __init__(self, error):
		self.error = error
	def __repr__(self):
		return(self.error)


class Rational:
	def __init__(self, numerator, denumerator):
		try:
			if not (isinstance(numerator, int) and isinstance(denumerator, int)):
				raise MyTypeError("wrong type")
		except MyTypeError as mte:
			print(mte)
		else:
			try:
				if denumerator==0:
					raise ZeroError("Can't devide to zero")
			except ZeroError as ze:
				ze.print_obj()
			else:
				self.numerator = numerator
				self.denumerator = denumerator

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
		numerator = self.normalize(self.numerator,self.numerator,self.denumerator)
		denumerator = self.normalize(self.denumerator,self.numerator,self.denumerator)
		return str(numerator) +" / "+ str(denumerator)

	def	__add__(self, other):
		x = self.numerator * other.denumerator+self.denumerator*other.numerator
		y = self.denumerator*other.denumerator
		try:
			if y==0:
				raise ZeroError("Can't devide to zero")
		except ZeroError as ze:
			ze.print_obj()
		else:
			return Rational(x,y)

	def	__sub__(self, other):
		x = self.numerator * other.denumerator-self.denumerator*other.numerator
		y = self.denumerator*other.denumerator
		try:
			if y==0:
				raise ZeroError("Can't devide to zero")
		except ZeroError as ze:
			ze.print_obj()
		else:
			return Rational(x,y)

	def	__mul__(self, other):
		x = self.numerator * other.numerator
		y = self.denumerator * other.denumerator
		try:
			if y==0:
				raise ZeroError("Can't devide to zero")
		except ZeroError as ze:
			ze.print_obj()
		else:
			return Rational(x,y)

	def	__div__(self, other):
		x = self.numerator / other.denumerator
		y = self.denumerator / other.numerator
		try:
			if y==0:
				raise ZeroError("Can't devide to zero")
		except ZeroError as ze:
			ze.print_obj()
		else:
			return Rational(x,y)

	def	__eq__(self, other):

		if self.numerator * other.denumerator == self.denumerator * other.numerator:
			return True
		else:
			return False

	def	__gt__(self, other):
		if self.numerator*other.denumerator>self.denumerator*other.numerator:
			return True
		else:
			return False

	def	__ge__(self, other):
		if self.numerator*other.denumerator>=self.denumerator*other.numerator:
			return True
		else:
			return False

	def	__lt__(self, other):
		if self.numerator*other.denumerator<self.denumerator*other.numerator:
			return True
		else:
			return False

	def	__le__(self, other):
		if self.numerator*other.denumerator<=self.denumerator*other.numerator:
			return True
		else:
			return False

	def __pow__(self, num):
		x = self.numerator**num
		y = self.denumerator**num
		return Rational(x,y)


a = Rational(2,1)
b = Rational(1,4)

print(a+b)

#print(b)