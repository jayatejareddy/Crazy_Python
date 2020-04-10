from Crypto.Util.Number import *
import random
m=raw_input('enter your secret message:')
n=748882771770214794518843198225720057648180155049
y=14354
c = []
bin_msg = bin(bytes_to_long(m))[2:]
for i in bin_msg:
	x = random.getrandbits(100)
	if (i == '1'):
		c.append((y*pow(x,3,n))%n)
	else:
		c.append(pow(x,3,n))
f = open('secret.txt','w')
f.write(str(c))
f.close()
print(c)
