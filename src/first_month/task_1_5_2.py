class Money():
	amount = 100
	currency = "USD"
	def __init__(self, amount, currency):
		self.amount = amount
		self.currency = currency
	def print_obj(self):
		return f"{self.amount} {self.currency}"
	def sum(self, other):
		obj = Money(self.amount+other.amount, self.currency)
		return obj
	def sub(self, other):
		obj = Money(self.amount-other.amount, self.currency)
		return obj




def main():
	x = Money(11, "USD")
	y = Money(5, "USD")
	print(x.print_obj())
	print(y.print_obj())
	print(x.sum(y).print_obj())
	print(x.sub(y).print_obj())
	#print(x+y)

main()