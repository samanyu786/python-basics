# 1. Write a program to calculate sum of Even number

n=int(input("enter number: "))
a=0

for i in range(n+1):
    if i%2==0:
        a=a+i
    else:
        continue
print(a)


# 1. Write a program to calculate sum of Even number

n=int(input("enter number: "))
a=0
i=1
while i<n+1:
    if i%2==0:
        a=a+i
        i+=1
    else:
        
print(a)


# 2. write a program to find the factorial of a number

fac=int(input("Enter the number: "))
res=1
i=1
while i<=fac:
    res=res*i
    i+=1
print(res)
    
    
# 2. write a program to find the factorial of a number

fac=int(input("Enter the number: "))

j=1
for i in range(1,fac+1):                          
    j=j*i
       
print(j)

# 3. write a program to check prime number

n=int(input("enter a number: "))
f=0
for i in range(2,n):
    if n%i==0:
        f=0
        break
    else:
        f=1
        continue
if f==0 and n!=2:
    print("the no is not prime")
elif f==1 or n==2:
    print("the no is prime")
       
