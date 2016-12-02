from decimal import *
import math
getcontext().prec = 40

def euclid_algo(b,a):
	r0 = a
	r1 = b
	r2 = 1
	ques=[]
	while(r2>0):
		q=r0/r1
		ques.append(q)
		r2 = r0 - q*r1
		r0=r1
		r1=r2
	return ques

def main():
	n = int(raw_input())
	b = int(raw_input())
	q = euclid_algo(n,b)
	c = [1,q[0]]
	d = [0,1]
	n1 = 0
	p1 = 0
	p2 = 0
	for j in range(1,len(q)):
		if c[j]!=0:
			n1 = (d[j]*b - 1)/c[j]
			if n1%1==0:
				prod = n-n1+1
				descrim = Decimal(prod*prod - 4*n)
				if descrim>=0:
					sqrtdesc = descrim.sqrt()
					if sqrtdesc._isinteger():
						p1 = (prod + sqrtdesc)
						p2 = (prod - sqrtdesc)
						if p1 % 2 ==0 and p2%2 ==0:
							p1 = p1/2
							p2 = p2 /2
						if p1>0 and p2>0:
							if p1<n and p2<n:
								print "p: ",p1," q: ",p2
								return 1
		c.append(q[j]*c[j]+c[j-1])
		d.append(q[j]*d[j]+d[j-1])
	print "Wiener's attack failed"
	return 0
main()	