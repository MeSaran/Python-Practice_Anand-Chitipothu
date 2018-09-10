def array(row,col):
	b = []
	c = []
	i = 0
	j = 0
	b = c
	#while(j < col):
	#	c.append('None')
	##	j+=1
	#print(c)
	#b.append(list(c))
	#print(b)
	while(i < row):	
		b.append(c)
		i+=1
	b[0].append('None')
	b[0].append('None')
	b[0].append('None')
	return b
a = array(2,3)
print(a) 
	
