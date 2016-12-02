import math, random

def gcd_ea(a,b):
	r0=a
	r1=b
	r2=1
	q=0
	while(r2!=0):
		q = r0/r1
		r2 = r0 - q*r1
		r0 = r1
		r1=r2
	return r0

def extended_ea(a,b):
	a0=a
	b0=b
	t0=0
	t=1
	temp=0
	q = a0/b0
	r = a0-q*b0
	while r>0:
		temp = (t0 - q*t)%a
		t0 = t
		t = temp
		a0 = b0
		b0 = r
		q = a0/b0
		r=a0 - q*b0
	if r!=0:
		return 0
	else:
		if(t<0):
			t = t+a
		return t

def param_gen(phi,n):
	a = 0.0
	a = math.pow(n,0.25)
	a = int(a/3)
	alist=[]
	params = []
	for i in range(1,a+1):
		alist.append(i)
	it = len(alist)
	while(it>0):
		if(it==1):
			random_ind = 0
		else:
			random_ind = random.randint(1,it-1)
		b = extended_ea(phi,alist[random_ind])
		if(gcd_ea(b,phi)==1 and b!=1):
			params.append(alist[random_ind])
			params.append(b)
			return params
		else:
			del alist[random_ind]
		it = len(alist)
	params.append(0)
	params.append(0)
	return params

def main():
	print "Enter prime number1: "
	p = int(raw_input())
	print "Enter prime number2: "
	q = int(raw_input())
	if(p>q):
		if p>2*q:
			print "Condition q<p<2q is not satisfied"
			return 0
	else:
		if q>2*p:
			print "Condition q<p<2q is not satisfied"
			return 0
	n = p*q
	phi = (p-1)*(q-1)
	param = param_gen(phi,n)
	print "Public Key: "
	print "b: ",param[1],"  n: ", n

main()
