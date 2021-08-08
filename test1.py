# python-basics

# USer enter any number and convert from KM to METER
n=int(input("Enter any number : "))
x=n*1000
print("The number in meter is :"+str(x))


# Enter 5 nos and find the greatest no
a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))
c=int(input("Enter 3rd no: "))
d=int(input("Enter 4th no: "))
e=int(input("Enter 5th no: "))

if a>b and a>c and a>d and a>e:
    print(str(a)+" is the largest no")
elif b>a and b>c and b>d and b>e:
    print(str(b)+" is the largest no")
elif c>a and c>b and c>d and c>e:
    print(str(c)+" is the largest no")
elif d>a and d>b and d>c and d>e:
    print(str(d)+" is the largest no")
else:
    print(str(e)+" is the largest no")


# Enter 5 subjects as input and more than 33 marks as pass and show grade.Sud not be >100 and <0
# 80 to 100- A
# 60 to 79- B
# 40 to 59-C
# 33 to 39-D
# O/t- Total Marks
#      Percentage:
#      Result: Pass or fail
# Grade:A

a=int(input("Enter marks in Hindi: "))
b=int(input("Enter marks in Eng: "))
c=int(input("Enter marks in Science: "))
d=int(input("Enter marks in Math: "))
e=int(input("Enter marks in SST: "))

if a>100 or a<0:
    print("Wrong no in Hindi")
    a=int(input("Correct no in Hindi: "))
if b>100 or b<0:
    print("Wrong no in Eng")
    b=int(input("Correct no in Eng: "))
if c>100 or c<0:
    print("Wrong no in Science")
    c=int(input("Correct no in Science: "))
if d>100 or d<0:
    print("Wrong no in Math")
    d=int(input("Correct no in Math: "))
if e>100 or e<0:
    print("Wrong no in SST")
    e=int(input("Correct no in SST: "))
  
tot_mark=a+b+c+d+e
av=(tot_mark/500)*100
print("Total marks:"+ str(tot_mark))

print("Percentage :"+ str(av)+"%")

if av <33:
    print("Result: "+"Fail")
else:
    print("Result:"+"Pass")
if av>=80 and av<=100:
    print("Grade:"+"A")
elif av>=60 and av<=79:
    print("Grade:"+"B")
elif av>=40 and av<=59:
    print("Grade:"+"C")
elif av>=33 and av<=39:
    print("Grade:"+"D")
else:
    quit
