""" Program to count the no of files(txt,py) """
import os
a = []
b = []
for fil in os.walk('/home/saran/trail/task18'):
	a.append(fil)
b = a[0][2]
p = 0
t = 0
for i in b:
	if i[-3:] == '.py':
		p+=1
	elif i[-4:] == '.txt':
		t+=1
print('No of .py file is %d'%(p))
print('No of .txt files is %d'%(t))
