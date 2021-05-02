class Rational:
	def __init__(self, x, y):
		self.numerator = x
		self.denumerator = y

	def gcd(self, a, b):
		while a != 0 and b != 0:
			if a > b:
				a = a % b
			else:
				b = b % a
		return a+b

	def lcm(self, a, b):
		great = 1
		if a>b:
			if a > b:
				great = a
			else:
				great = b
		while True:
			if great % a ==0 and great % b ==0:
				lcm = great
				break
			great +=1
		return lcm

	def __repr__(self):
		z = self.gcd(self.numerator, self.denumerator)
		return str(self.numerator//z) +" / "+ str(self.denumerator//z)

	def	__add__(self, other):
		z = self.gcd(self.numerator, self.denumerator)
		lcm = self.lcm(self.numerator, self.denumerator)
		x = lcm//self.denumerator*self.numerator+lcm//other.denumerator*other.numerator
		return Rational(x//z, lcm//z)

	def	__sub__(self, other):
		z = self.gcd(self.numerator, self.denumerator)
		lcm = self.lcm(self.numerator, self.denumerator)
		x = lcm//self.denumerator*self.numerator-lcm//other.denumerator*other.numerator
		return Rational(x//z, lcm//z)

	def	__mul__(self, other):
		z = self.gcd(self.numerator, self.denumerator)
		x = self.numerator * other.numerator
		y = self.denumerator * other.denumerator
		return Rational(x//z, y//z)

	def	__div__(self, other):
		z = self.gcd(self.numerator, self.denumerator)
		x = self.numerator * other.denumerator
		y = self.denumerator * other.numerator
		return Rational(x//z, y//z)

	def	__eq__(self, other):
		i = self.gcd(self.numerator, self.denumerator)
		j = self.gcd(other.numerator, other.denumerator)
		if self.numerator/i == other.numerator/j and self.denumerator/i == other.denumerator/j:
			return True
		else:
			return False

	def	__gt__(self, other):
		lcm = self.lcm(self.numerator, self.denumerator)
		if lcm//self.denumerator*self.numerator>lcm//other.denumerator*other.numerator:
			return True
		else:
			return False

	def	__gte__(self, other):
		lcm = self.lcm(self.numerator, self.denumerator)
		if lcm//self.denumerator*self.numerator>=lcm//other.denumerator*other.numerator:
			return True
		else:
			return False

	def	__lt__(self, other):
		lcm = self.lcm(self.numerator, self.denumerator)
		if lcm//self.denumerator*self.numerator<lcm//other.denumerator*other.numerator:
			return True
		else:
			return False

	def	__lte__(self, other):
		lcm = self.lcm(self.numerator, self.denumerator)
		if lcm//self.denumerator*self.numerator<=lcm//other.denumerator*other.numerator:
			return True
		else:
			return False





a = Rational(100,20)
b = Rational(25,5)

print(a+b)
print(a-b)
print(a*b)
print(a==b)
print(a>=b)



