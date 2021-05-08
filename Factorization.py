import math
import time
import random

#trial division factorization.........
def trial_division_factorization(n):
 print("\nTrial division factorization : \n")
 start=time.clock()
 a=2
 l=[]
 while(a<=(math.sqrt(n))):
  while(n%a==0):
   l.append(a)
   n=n/a
  a=a+1

 if (n>1):
  l.append(int(n))
 tym=(time.clock()-start)
 print("Time taken for calculating factors is",tym*(10**6),"microseconds")
 t=[str(i) for i in l]
 print("FActors are : ",'*'.join(t))
 for x in l:
  print(x,"is",miller_rabin(x))
 for x in l:
  print("Time taken to test for primality of ",x," is",miller_rabin_time(x),"microsecomds")
 print("...........................")

#function to find gcd of a number......

def gcd(a,b):
 while b:
  a,b=b,a%b
 return a

#pollard p-1 factorization.........

def pollard_p(n):
 print("Pollard p-1 factorization : \n")
 start=time.clock()
 a=2
 e=2
 while(e<=int(n**.5) and a!=1):
  b=a
  a=(a**e) % n
  e=e+1

 p=gcd(b-1,n)
 
 if (1<=p<=n):
  print("Factors are : ", p,"*",n//p)
 else:
  print("failure")
 l=[]
 l.append(p)
 l.append(n//p)
 for x in l:
  print(x,"is",miller_rabin(x))
 print("Time taken for calculating factors is : ",(time.clock()-start)*(10**6),"microseconds")
 for x in l:
  print("Time taken to test for primality of ",x,"is",miller_rabin_time(x),"microsecomds")
 print("..........................")


#fermat faactorization.......

def fermat(n):
 print("Fermat Factorization : \n")
 start=time.clock()
 x=int(n**.5)+1
 w=x*x-n
 z=int(w**.5)
 while(z*z!=w):
   x+=1
   w=x*x-n
   z=int(w**.5)
 a=x+z
 b=x-z
 print("Factors are : ",a,"*",b)
 x=x+1
 l=[]
 l.append(a)
 l.append(b)
 for x in l:
  print(x,"is",miller_rabin(x))
 print("Time taken for calculating factors is : ",(time.clock()-start)*(10**6),"microseconds")
 for x in l:
  print("Time taken to test for primality of ",x," is",miller_rabin_time(x),"microsecomds")
 print("..........................") 

#function to find factorial....
 
def fact(n):
 if (n==1 or n==0):
  return 1
 else:
  return n*fact(n-1)

#pollard rho factorization........

def pollard(n):
 print("Pollard rho Factorization : \n")
 start=time.clock()
 if(n%2==0):
  print( 2)
 x=2
 y=x
 d=1
 while(d==1):
  x=(x*x+1)%n
  y=(y*y+1)%n
  y=(y*y+1)%n
  d=gcd(x-y,n)
  if(d==n):
   break
 print("Time taken for calculating factors are : ",(time.clock()-start)*(10**6),"microseconds")
 l=[]
 print("Factors are : ",d,"*",n//d)
 l.append(int(d))
 l.append(int(n/d))
 for x in l:
  print(x,"is",miller_rabin(x))
 for x in l:
  print("Time taken to test for primality of ",x," is",miller_rabin_time(x),"microsecomds")

 
#primality testing by miller rabin test.........

def miller_rabin(p):
 start=time.time()
 if(p<2):
  return(" Not a prime")
 
 if(p!=2 and p%2==0):
  return(" Not a prime")

 s=p-1
 while(s%2==0):
  s>>=1
 for i in range(10):
  a=random.randrange(p-1)+1
  temp=s
  mod=pow(a,temp,p)
  while(temp!=p-1 and mod!=1 and mod!=p-1):
   mod=(mod*mod)%2
   temp=temp*2
  if(mod!=p-1 and temp%2==0):
   return(" Not a prime")
  
   
 return("Prime")
 
#miller rabin test time .........

def miller_rabin_time(p):
 start=time.time()
 if(p<2):
  return((time.time()-start)*(10**6))
 
 if(p!=2 and p%2==0):
  return((time.time().start)*(10**6))

 s=p-1
 while(s%2==0):
  s>>=1
 for i in range(10):
  a=random.randrange(p-1)+1
  temp=s
  mod=pow(a,temp,p)
  while(temp!=p-1 and mod!=1 and mod!=p-1):
   mod=(mod*mod)%2
   temp=temp*2
  if(mod!=p-1 and temp%2==0):
   return((time.time()-start)*(10**6))
  
   
 return((time.time()-start)*(10**6))
 



#main method......

def main():
 n=int(input("Enter a positive integer : "))
 trial_division_factorization(n)
 fermat(n)
 pollard_p(n)
 pollard(n)
 print (miller_rabin(n))




if __name__=='__main__':
 main()
