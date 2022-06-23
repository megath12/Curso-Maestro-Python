#import sys
#print(sys.argv[1:])

import sys
#print(sys.argv) # argumentos enviado
if len(sys.argv)==2:
	fila=int(sys.argv[1])
	l=1
	k=fila
	while fila>10**l:
		l+=1
	l-=1
	for i in range(l,-1,-1):
		j=k//10**i
		u=j*10**i
		print("{:06d}".format(u))
		k=k-u
		
else:
	print("Escribe lo que se te pide!!")


