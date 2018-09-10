class xrange():
	def __init__(self,n):
		self.i = 0
		self.n = n
	def __itit__(self):
		return self
	def next(self):
		if self.i < self.n:
			i = self.n
			self.n -= 1
			return i
		else:
			raise StopIteration()
a = xrange(4)
print(a.next())
print(a.next())
print(a.next())
#print(sum(xrange(5)))
