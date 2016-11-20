


GLOBAL_VALUE = [1,2,3]
class person():

	def __init__(self, name):
		self.name = name

	def method(self):
		print ("fuck you {}".format(self.name))

	def print_name(self, name):
		print (name)


bill = person('bill')

bill.method()

print(bill.name)

bill.name = "not bill"

print (bill.name)

bill.temp_name = list(GLOBAL_VALUE)


bill.temp_name.remove(1)

print (bill.temp_name)
print (GLOBAL_VALUE)


# I want to create an object
# Pass in a value and not change anything