#word count in file
line = len(open('frst.txt').readlines())
print(line)
wrd = len(open('frst.txt').read().split())
print(wrd)
ch = len(open('frst.txt').read())
print(ch)
sent = open('frst.txt').read()
print('Original')
print(sent)
print('--------------------------')
a = sent.split('.')
a.reverse()
#print(a)
#a = "".join(list(sent)).split()
#a.reverse()
b = " ".join(a)
print(b)
