def max_x():
    a=[2,5,7,9,8,6,4,3]
    i=0
    max=0
    sec_m=0
    third_m=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[j]>=max:
               max=a[j]
            if a[j]>sec_m and a[j] !=max:
                sec_m=a[j]
            if a[i]>third_m and a[i]!=max and a[i]!=sec_m:
                third_m=a[i]
            j=j+1
            i=i+1
    print(max)
    print(sec_m)
    print(third_m)
max_x()