file_name=input('enter encrypted file name')
f=open(file_name,'r')
cipher=f.read()
cipher=cipher[1:len(cipher)-1:]
cipher=cipher.split(', ')
n=748882771770214794518843198225720057648180155049
p=716158806799958648435521
q=1045693726949303272312169
message=''
phin=(p-1)*(q-1)
for i in cipher:
	i=long(i)
	if pow(i,phin/3,n)==1:
		message=message+'0'
	else:
	    message=message+'1'
secret=hex(int(message,2))
secret=secret[2:len(secret)-1:]
print('the secret message is:'+secret.decode('hex'))
