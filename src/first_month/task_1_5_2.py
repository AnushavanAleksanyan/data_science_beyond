class Money():
	amount = 100
	currency = "USD"
	def __init__(self, amount, currency):
		self.amount = amount
		self.currency = currency
	def print_obj(self):
		return self.amount, self.currency
	def sum(self, other):
		return self.amount + other.amount
	def sub(self, other):
		return self.amount - other.amount
	def __repr__(self):
		return f"{self.amount} {self.currency}"



def main():
	x = Money(11, "USD")
	y = Money(5, "USD")
	print(x)
	print(y)
	print(x.sum(y))
	print(x.sub(y))

main()