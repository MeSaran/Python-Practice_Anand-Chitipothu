a = [1, 2, 3, 4, 5]
a.sort()
n = int((len(a) / 2)) + 1
b = []
def triplets(a,n):
	for i in range(0,n):
		for j in range(i+1,n):
			b.append((a[i],a[j],a[i]+a[j]))
triplets(a,n)
print(b)
