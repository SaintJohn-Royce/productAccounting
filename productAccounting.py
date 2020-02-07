products = []

while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('and the price of the item? ')
	
	p = []
	p.append(name)
	p.append(price)
	
	# an easier way is to write p = [name, price]

	products.append(p)

	# a further easier way is to write products.append([name, price])

print(products)

for p in products:
	print(p[0], 'has a price of', p[1])