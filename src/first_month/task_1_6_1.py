# Class - Rational
# def gcd(a, b):
# 	while a != 0 and b != 0:
# 		if a > b:
# 			a = a % b
# 		else:
# 			b = b % a
# 	return a+b


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
		pass

	def __repr__(self):
		z = self.gcd(self.numerator, self.denumerator)
		return str(self.numerator//z) +" / "+ str(self.denumerator//z)

	def	__add__(self, other):
		lcm = self.lcm(self.numerator, self.denumerator)
		return lcm//self.denumerator*self.numerator+lcm//other.denumerator*other.numerator, lcm






a = Rational(9,10)
b = Rational(1,6)
print(a)