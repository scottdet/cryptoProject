import numpy

if __name__ == "__main__":
	with open('ticker.txt') as temp_file:
		ticker = [line.rstrip('\n').split(",") for line in temp_file]
		prices={}
		for line in ticker:
			if line[0] in prices:
				prices[line[0]].append(line[2])
			else:
				list=[]
				list.append(line[2])
				prices[line[0]] = list

		for key1, values1 in prices.iteritems():
			for key2, values2 in prices.iteritems():
				if key1 != key2:
					# (list1.append(int(entry)) for entry in values1)
					# (list2.append(int(entry)) for entry in values1)
					x = numpy.corrcoef(map(float, values1), map(float, values2))[0][1]
					if x > 0.95 or x < -0.95:
						print key1, key2, x

		print prices["Bitcoin"]
		print prices["Iconomi"]
		print prices["Dash"]
		print prices["Augur"]
		print prices["Golem"]
		print prices["Round"]

	#print prices
