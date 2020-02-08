products = []
totalPrice = 0

while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('and the price of the item (in integer)? ')
	priceInt = int(price)
	itemNumber = input('how many of these would you like: ')
	itemNumberInt = int(itemNumber)
	itemTotalPriceInt = priceInt * itemNumberInt
	totalPrice = totalPrice + itemTotalPriceInt

	#p = []
	#p.append(name)
	#p.append(price)
	#p.append(itemNumber)

	products.append([name, price, itemNumber, str(itemTotalPriceInt)])

# display methods
#for p in products:
#	print(p[0], p[1], p[2], p[3])

# write in a 'file' known as 'product.csv'
# in the event that chinese is used, insert encoding = 'utf-8', as in:
# with open('product.csv', 'w', encoding = 'utf-8') as file:
with open('product.csv', 'w') as file:

	file.write('Item name, Individual Price, Number of Items, Total Item Price\n')

	# for every line 'p' in 'products'
	for p in products:

		# it is written in 'file' the content from each line 'p' 
		# with the additions
		file.write(p[0] + ',' + p[1] + ',' + p[2] + ',' + p[3] + '\n')

	file.write(',' + ',' + 'Total Price: ' + ',' + str(totalPrice))


