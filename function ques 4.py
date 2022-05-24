def checknumber_list():
    a=[2,3,4,5,6,6]
    b=[4,5,6,7,88,5]
    i=0
    while i<len(a):
        if  a[i]%2==0:
            if b[i]%2==0:
                print("both are even")
        else:
            print("both are not even")
        i=i+1
checknumber_list()
