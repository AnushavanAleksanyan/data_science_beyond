class Money():
	amount = 100
	currency = "USD"
	def __init__(self, amount, currency):
		self.amount = amount
		self.currency = currency
	def print_obj(self):
		print(self.amount, self.currency)
	def sum(self, other):
		return self.amount + other.amount
	def sub(self, other):
		return self.amount - other.amount




def main():
	x = Money(11, "USD")
	y = Money(5, "USD")
	x.print_obj()
	y.print_obj()
	print(x.sum(y))
	print(x.sub(y))

main()