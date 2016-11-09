from classes import Attribute, Instance, LGGConj

def main():
	#Array of class
	instances = []
	
	#Read file and append instances to instance list
	file = open('instances.txt')
	for line in file:
		token = line.split("/")
		ins = Instance(token[0])
		
		for i in range(1,len(token)):
			attrToken = token[i].split("=")
			attr = Attribute(attrToken[0], attrToken[1])
			ins.addAttribute(attr)	
		
		instances.append(ins)
	
	expression = instances[0]
	instances.pop(0)

	expression = LGGConj(expression, instances)	

	print "Least general generalisation of set using LGG-Conj algorithm (4.2): " + str(expression)
	return 0


if __name__ == "__main__":
	main()
