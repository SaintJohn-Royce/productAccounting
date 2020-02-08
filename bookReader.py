products = []

with open('product.csv', 'r') as file:

	for line in file:

		# strip: recognizes that there is a '\n' and removes all of them
		# split: recognizes that the splits occur at the commas
		# thus, this code removes all of the '\n' and then splits by commas
		#strip = line.strip().split(',')

		#name = strip[0]
		#price = strip[1]
		# a faster way is to write
		name, price, itemNumber, itemTotalPriceStr = line.strip().split(',')

		products.append([name, price, itemNumber, itemTotalPriceStr])

print(products)