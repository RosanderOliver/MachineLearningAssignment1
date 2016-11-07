class Attribute:
	expression = ""
	bool = False

	def __init__(self, exp, bo):
		self.expression = exp
		self.bool = bo

	def __str__(self):
		return str(self.bool) + " " + self.expression   
