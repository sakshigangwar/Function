def multiple(a,b):
    i=0
    multiply=0
    x=[]
    while i<len(a):
        multiply=a[i]*b[i]
        x.append(multiply)
        i=i+1
    print(x)
multiple([5, 10, 50, 20], [2, 20, 3, 5])
