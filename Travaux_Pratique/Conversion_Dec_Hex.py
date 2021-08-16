def darstell(my_list, rest):
	if rest == 10 :
		my_list.append('A')
	elif rest == 11 :
		my_list.append('B')
	elif rest == 12:
		my_list.append('C')
	elif rest == 13 :
		my_list.append('D')
	elif rest == 14:
		my_list.append('E')
	elif rest == 15:
		my_list.append('F')
	else:
		my_list.append(rest)
my_list = list()
number = int(input('Geben einen Nummer ein: '))
quotient= number//16
rest = number%16
darstell(my_list, rest)
while quotient !=0:
	rest = quotient%16
	quotient = quotient // 16
	darstell(my_list, rest)
c = ''
my_list.reverse()
for elt in my_list:
	c = c + str(elt)
print('Umwandlung von {} ist : {}'.format(number, c))
