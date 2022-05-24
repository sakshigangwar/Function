def function(a): 
    a="The quick Brow Fox"
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>"A" and a[i]<"Z":
            c=c+1
        else:
            c1=c1+1
        i=i+1
    print("uper case=",c)
    print("lower case",c1)
function("The quick Brow Fox")


