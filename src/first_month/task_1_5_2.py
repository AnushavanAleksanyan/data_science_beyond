class Money():
	rates = {"USD": 523, "EUR": 631, "RUB": 7.05, "AMD":1}
	def __init__(self, amount, currency):
		self.amount = amount
		self.currency = currency
	def __repr__(self):
		return f"{self.amount} {self.currency}"
	def sum(self, other):
		obj = Money(self.amount+other.amount, self.currency)
		return obj
	def change(self, rate):
		obj = Money(self.amount*self.rates[self.currency]/self.rates[rate], rate)
		return obj
	def sub(self, other):
		obj = Money(self.amount-other.amount, self.currency)
		return obj



def main():
	x = Money(10, "USD")
	y = Money(5, "USD")
	z = Money(10, 'EUR')
	# print(x.print_obj())
	# print(y.print_obj())
	# print(x.sum(y).print_obj())
	# print(x.sub(y).print_obj())
	#print(z.change("USD").print_obj())

main()