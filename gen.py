# 2-16
k=8
n=2**k-1
players=n+1
i2=0
f=open('input.txt','w')
f.write(str(n)+'\n')
while i2<k:
	i1=1
	while i1<=players:
		step=2**i2
		f.write(str(i1))
		f.write(" "+str(i1+step)+'\n')
		i1+=2*step
	i2+=1
