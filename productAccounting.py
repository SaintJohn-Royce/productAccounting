products = []

while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('and the price of the item? ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

print(products[0][0])