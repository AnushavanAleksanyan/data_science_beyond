class MinusError(Exception):
	def __init__(self, err_text, val):
		self.err_text = err_text
		self.val = val
	def print_obj(self):
		print(self.err_text, "|", self.val)

class MyTypeError(Exception):
	def __init__(self, error):
		self.error = error
	def __repr__(self):
		return(self.error)

class Money():
	rates = {"USD": 523, "EUR": 631, "RUB": 7.05, "AMD": 1}

	def __init__(self, amount:int, currency:str):
		try:
			if int(amount)<0:
				raise MinusError("Amount is less than 0", amount)
		except MinusError as me:
			me.print_obj()
		else:
			try:
				if not (isinstance(amount, int) and isinstance(currency, str)):
					raise MyTypeError("Type Error")
			except MyTypeError as mte:
				print(mte)
			else:
				self.amount = amount
				self.currency = currency

	def __repr__(self):
		return f"{self.amount} {self.currency}"

	def sum(self, other):
		obj = Money(self.amount+other.amount, self.currency)
		return obj

	def change(self, rate):
		obj = Money(
			self.amount*self.rates[self.currency]/self.rates[rate], rate)
		return obj

	def sub(self, other):
		result = self.amount-other.amount
		try:
			if result<=0:
				raise MinusError("result can't be negative", result)
		except MinusError as me:
			me.print_obj()
		else:
			obj = Money(self.amount-other.amount, self.currency)
			return obj



def main():
	x = Money(9, 10)
	y = Money(5, "USD")
	z = Money(10, 'EUR')
	print(x)
    # print(y.print_obj())
	# print(x.sum(y))
	print(x.sub(y))
	# print(z.change("USD").print_obj())


main()