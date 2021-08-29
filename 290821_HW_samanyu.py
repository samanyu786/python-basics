while True:
    r=int(input("enter roll no: "))
    n=input("enter name: ")
    a=input("enter addr: ")
    m=int(input("enter mob no: "))
    print("1 Add")
    print("2 Modify by roll")
    print("3 Delete by roll")
    print("4 Search by mob")
    print("5 Search by name")
    print("6 Search by roll")
    print("7 List Record")
    print("8 Exit")
    usr=int(input("enter your choice: "))
    c=[]
    c.append(r)
    c.append(n)
    c.append(a)
    c.append(m)

    if usr==1:
        print(c)
        
    elif usr==2:
        c[0]=2
        print(c)
    elif usr==3:
        c.remove(c[0])
        print(c)
    elif usr==4:
        mob=int(input("search this mob no: "))
        if m==mob:
            print("found")
        else:
            print("not found")
    elif usr==5:
        nm=input("search this name: ")
        if n==nm:
            print("found")
        else:
            print("not found")
    elif usr==6:
        rl=int(input("search this roll no: "))
        if r==rl:
            print("found")
        else:
            print("not found")
    elif usr==7:
        print("unable to understand what list is required")
    else:
        break

    
