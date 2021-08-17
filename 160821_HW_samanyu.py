# 1. Write a Python program to find the largest number among the five input numbers using elif

a=int(input("Enter the 1st no: "))
b=int(input("Enter the 2nd no: "))
c=int(input("Enter the 3rd no: "))
d=int(input("Enter the 4th no: "))
e=int(input("Enter the 5th no: "))

if a>b and a>c and a>d and a>e:
    print("The largest no is "+ str(a))
elif b>c and b>d and b>e:
    print("The largest no is "+ str(b))
elif c>d and c>e:
    print("The largest no is "+ str(c))
elif d>e:
    print("The largest no is "+ str(d))
else:
    print("The largest no is "+ str(e))
    
# 2. Write a python program input any charactor and Check Whether a Character is a Vowel or Consonantin

char=input("Enter any character: ")

if char=="a" or char=="A" or char=="e" or char=="E" or char=="i" or char=="I" or char=="o" or char=="O" or char=="u" or char=="U":
    print("The character is vowel")
else:
    print("The character is consonant")
