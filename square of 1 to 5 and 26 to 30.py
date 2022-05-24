def square():
    i=0
    b=[]
    m=[]
    while i<=5:
        c=i*i
        b.append(c)
        i=i+1
    print(b)
    j=26
    k=[]
    while j<=30:
        d=j*j
        k.append(d)
        j=j+1
    print(k)
    m.append(b)
    m.append(k)
    print(m)
square()