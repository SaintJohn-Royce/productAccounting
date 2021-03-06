import os # operating system

filename = input('please input desired file name with .csv: ')

def read_file(filename):

	products = []

	with open(filename, 'r') as file:

		for line in file:

			if 'Item Name' in line:

				continue #jump to next step of the for loop

				# strip: recognizes that there is a '\n' and removes all of them
				# split: recognizes that the splits occur at the commas
				# thus, this code removes all of the '\n' and then splits by commas
				#strip = line.strip().split(',')

				#name = strip[0]
				#price = strip[1]
				# a faster way is to write
			name, price, itemNumber, itemTotalPriceStr = line.strip().split(',')

			products.append([name, price, itemNumber, itemTotalPriceStr])

	return products

def main(filename):
	if os.path.isfile(filename):

		print('the file', filename, 'exists')

		products = read_file(filename)

		print(products)

	else:

		print('this file does not exist')

main(filename)