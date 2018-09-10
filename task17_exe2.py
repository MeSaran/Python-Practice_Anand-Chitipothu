#using textwrapZZ
import textwrap
f = open('frst.txt').read()
wrp = textwrap.TextWrapper(width=20)
strng = wrp.fill(text=f)
print(strng)

