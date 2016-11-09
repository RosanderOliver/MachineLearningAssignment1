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
		st = ""
		for at in self.attributes:
			if at != self.attributes[len(self.attributes)-1]:
				st += str(at) + " AND "
			else:
				st += str(at)
		return st

	def remove(self, attr):
		self.attributes.remove(attr)


def LGGConj(gen, ins):
	#Do algorithm 4.2 AND 4.3
	
	for i in ins:
		for x in i.attributes:
			for g in gen.attributes:
				if (g.expression == x.expression) and (g.value != x.value):
					#remove expressions from g
					gen.remove(g)

	return gen
