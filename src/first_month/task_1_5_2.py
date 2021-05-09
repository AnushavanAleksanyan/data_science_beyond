class MoneyClassError(Exception):
	def __init__(self, err_text, val):
		self.err_text = err_text
		self.val = val
	def print_obj(self):
		print(self.err_text, "|", self.val)


class Money():
	rates = {"USD": 523, "EUR": 631, "RUB": 7.05, "AMD": 1}

	def __init__(self, amount:int, currency:str):
		try:
			if int(amount)<0:
				raise MoneyClassError("Amount is less than 0", amount)
		except MoneyClassError as me:
			me.print_obj()
		else:
			try:
				if not isinstance(currency, str):
					raise MoneyClassError("currency must be string", currency)
				elif not isinstance(amount, int):
					raise MoneyClassError("amount must be number", amount)
			except MoneyClassError as te:
				te.print_obj()
			else:
				self.__amount = amount
				self.__currency = currency

	def __repr__(self):
		return f"{self.__amount} {self.__currency}"

	def get_amount(self):
		print("get")
		return self.__amount

	def set_amount(self, x):
		try:
			if x<0:
				raise MoneyClassError("Amount is less than 0", x)
		except MoneyClassError as me:
			me.print_obj()
		else:
			print("set")
			self.__amount = x

	def del_amount(self):
		print("del")
		del self.__amount

	amount = property(get_amount, set_amount, del_amount, doc = "property for amount")

	def __add__(self, other):
		obj = Money(self.__amount+other.__amount, self.__currency)
		return obj

	def change(self, rate):
		obj = Money(self.__amount*self.rates[self.__currency]/self.rates[rate], rate)
		return obj

	def __sub__(self, other):
		result = self.__amount-other.__amount
		try:
			if result<=0:
				raise MoneyClassError("result can't be negative", result)
		except MoneyClassError as me:
			me.print_obj()
		else:
			obj = Money(self.__amount-other.__amount, self.__currency)
			return obj



def main():
	x = Money(9, "usd")
	y = Money(5, "USD")
	z = Money(10, 'EUR')
	# print(x.amount)
	# x.amount = -10
	# print(x.amount)
	# print(x+y)
	# print(x.sub(y))
	# print(z.change("USD").print_obj())


#main()