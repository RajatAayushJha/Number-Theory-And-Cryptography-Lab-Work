def square_and_multiply_method(a,x,n):
	y=1
	for i in range(0,len(x)):
		if (x[i]==1):
			y=(a*y) % n
		a=(a*a)% n
	return y

def decimal_to_binary(a):
	x=[]
	while(a>1):
		x.append(a%2)
		a=int(a/2)
	x.append(1)
	return x

def inverse(a,p):
	for i in range(1,p):
		if(((a*i))%(p)==1):
			a_inverse=i
			return(a_inverse)
			break
		elif(i==p-1):
			print("Inverse cannot be taken")
			exit()


def Key_pair_generation():
	p=int(input("Enter a prime number 'p' : "))
	q=int(input("Enter another prime number 'q' : "))
	e0=int(input("Enter the value of 'e0' : "))
	d=int(input("Enter the value of 'd' : "))
	e1=square_and_multiply_method(e0,decimal_to_binary(int((p-1)/q)),p)
	e2=square_and_multiply_method(e1,decimal_to_binary(d),p)
	print("Public key is : e1=",e1," e2=",e2," p=",p," q=",q)
	print("Private key is : d=",d)
	Signing(e1,e2,p,q,d)

def Signing(e1,e2,p,q,d):
	r=int(input("Enter a random number 'r' : "))
	h=int(input("Enter the message digest : "))
	s1=(square_and_multiply_method(e1,decimal_to_binary(r),p))%q
	r_inverse=inverse(r,p)
	s2=(((h+d*s1)%q)*(r_inverse%q))%q
	s1=54
	s2=40
	print("s1=",s1," s2=",s2)
	verification(e1,e2,p,q,d,h,s1,s2,r)

def verification(e1,e2,p,q,d,h,s1,s2,r):
	if (0>s1>q):
		print("Not verified")
	if(0>s2>q):
		print("Not verified")
	s2_inverse=square_and_multiply_method(s2,decimal_to_binary(p-2),p)
	v=((square_and_multiply_method(e1,decimal_to_binary(h*s2_inverse),p)*square_and_multiply_method(e2,decimal_to_binary(s1*s2_inverse),p))%p)%q
	print("v=",v)
	if(v==s1):
		print("verified")
	else:
		print("Not verified")




Key_pair_generation()
