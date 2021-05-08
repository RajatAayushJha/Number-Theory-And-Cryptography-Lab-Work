import random
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

def is_prime(num) :
	if num <= 1 :
		return False
	if num <= 3 :
		return True
	if num%2 == 0 or num%3 == 0 :
		return False
	for i in range(5,int(num**0.5)+1,6) :
		if num%i == 0 or num%(i+2) == 0 :
			return False
	return True

def primitive_root(p):
	if p==2:
		return 1
	p1=2
	p2=(p-1)//p1
	while(1):
		g=random.randint(2,p-1)
		if not(square_and_multiply_method(g,decimal_to_binary((p-1)//p1),p)==1):
			if not (square_and_multiply_method(g,decimal_to_binary((p-1)//p1),p)==1):
				return g

def ElGlamal_key_generation():
	print("In keys Generation phase...")
	p=int(input("Enter a prime number : "))
	e1=primitive_root(p)
	d=int(input("Enter d : "))
	e2=square_and_multiply_method(e1,decimal_to_binary(d),p)
	print("Public keys : e1=",e1," e2=",e2," p=",p)
	print("Private keys : d=",d)
	return(e1,e2,p)

def signature_generation():
	print()
	print("In Signature Generation phase ....")
	m=input("Enter message : ")
	sum=0
	for symb in m:
		sum=sum+ord(symb)
	d=int(input("Enter private key : "))
	e1=int(input("Enter e1 : "))
	e2=int(input("Enter e2 : "))
	p=int(input("Enter p : "))
	r=int(input("Enter r : "))
	s1=square_and_multiply_method(e1,decimal_to_binary(r),p)
	for i in range(1,p-1):
		if(((r*i))%(p-1)==1):
			r_inverse=i
			break
		elif(i==p-2):
			print("Inverse cannot be taken")
			r_inverse=1
	
	s2=(((sum-d*s1)%(p-1))*(r_inverse)%(p-1))%(p-1)
	print("Signatures are : ")
	print(s1,s2)
	l=[m,s1,s2,p,e1,e2]
	return(l)

def verification():
	print()
	print("In Signature verification phase ....")
	m=input("Enter message : ")
	e1=int(input("Enter e1 : "))
	e2=int(input("Enter e2 : "))
	p=int(input("Enter p : "))
	s1=int(input("Enter first signature : "))
	s2=int(input("Enter second signature : "))
	sum=0
	for symb in m:
		sum=sum+ord(symb)
	v1=square_and_multiply_method(e1,decimal_to_binary(int(sum)),p)
	v2=(square_and_multiply_method(e2,decimal_to_binary(s1),p)*square_and_multiply_method(s1,decimal_to_binary(s2),p))%p
	print("v1=",v1," v2=",v2)
	
	if(0>s1>p):
		return("Error in verification")
	elif(0>s2>p):
		return("Error in verification")
	elif(v1%p!=v2%p):
		return ("Error in verification")
	else:
		return("Signature Verified")



ElGlamal_key_generation()
signature_generation()
print(verification())
