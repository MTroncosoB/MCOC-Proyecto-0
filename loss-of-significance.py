import scipy as sp


x = [1.73*(10**-6), 5.84*(10**-7), 2.38*(10**-8)]
L=len(x)

#Resultados para 64 bits

R_64 = []
for j in x:
	j_64 = sp.float64((i**3)-1.0)
	R_64.append(j_64)

#Resultado exacto por calculadora
resultado_calculadora = [-0.999999999999999994822283, -0.999999999999999999800823296, -0.999999999999999999999986518728]

#Error

Error=[]

k=0
while k < L:
	Error.append((abs(R_64[k]-resultado_calculadora[k]))/resultado_calculadora[k])
	k+=1


print "resultado float 64:", R_64
print "resultado calculadora:",resultado_calculadora
print "Error:", Error
