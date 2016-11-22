class Attribute:
	def __init__(self, exp, va):
		self.value = []
		self.expression = exp
		self.value.append(va.rstrip())

	def __str__(self):
		return self.expression + "=" + str(self.value) 
	
	def addValue(self, nv):
		exists = nv[0] in self.value
		if not exists:
			self.value.append(nv[0])		


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
	
	for x in ins.attributes:
		for g in gen.attributes:
			if (g.expression == x.expression) and (g.value != x.value):
				#remove expressions from g
				gen.remove(g)
	return gen

def LGGConjID(gen, ins):
	for x in range(0,len(gen.attributes)-1):
		if (gen.attributes[x].expression == ins.attributes[x].expression) \
		and gen.attributes[x].value != ins.attributes[x].value:
			gen.attributes[x].addValue(ins.attributes[x].value)
			print "Added value"
	return gen
