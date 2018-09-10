""" Program to show the tree structure i file system """
import os
for root,dirr,files in os.walk('.',topdown=False):
	for name in files:
		print(os.path.join(root,name))
	for name in dirr:
		print(os.path.join(root,name))

