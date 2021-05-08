import random 
import hashlib
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

def verification(m,s1,s2,e1,e2,s_1):
	a=square_and_multiply_method(e1,decimal_to_binary(int(s2)),p)
	e2_inverse=0
	for i in range(1,p-1):
		if(((e2*i))%(p-1)==1):
			e2_inverse=i
			print("shreya")
			break
		elif(i==p-2):
			print("Inverse cannot be taken")
			exit()

	d=e2_inverse**s_1
	c=(a*d)%p
	print(a,d)
	e=c%p
	str1=m+str(e)
	print(str1)
	encoded_msg=hashlib.md5(str1.encode())
	v1=encoded_msg.hexdigest()
	v=0
	for symb in v1:
		v+=ord(symb)
	if s_1==v%p:
		print("Verified")
	else:
		print("Not Verified")

p=int(input("Enter a prime number 'p' : "))
q=int(input("Enter another prime 'q' : "))
e0=int(input("Enter the value of 'e0' : "))
d=int(input("Enter the value of d : "))
M=input("Enter message : ")
r=11
e1=square_and_multiply_method(e0,decimal_to_binary(int((p-1)/q)),p)
e2=square_and_multiply_method(e1,decimal_to_binary(d),p)
print("e1 = ",e1," e2= ",e2)
str2=M+str(square_and_multiply_method(e1,decimal_to_binary(r),p))
encoded_msg=hashlib.md5(str2.encode())
s1=encoded_msg.hexdigest()
s_1=0
for symb in s1:
	s_1+=ord(symb)
print("s1=",s_1)
s2=r+(d*s_1)%q

verification(M,s1,s2,e1,e2,s_1)
