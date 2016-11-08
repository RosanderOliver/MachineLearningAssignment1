class Attribute:
	def __init__(self, exp, va):
		self.expression = exp
		self.value = va

	def __str__(self):
		return self.expression + "=" + str(self.value) 

class Instance:
	def __init__(self, ca):
		self.case = ca
		self.attributes = []

	def addAttribute(self, attr):
		self.attributes.append(attr)  

	def __str__(self):
		st = str(self.case) + "; "
		for at in self.attributes:
			st += str(at) + " "
		return st
	def LGG:
		return 0
