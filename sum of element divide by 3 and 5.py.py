def func(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum)
func(23)



def sum():
    a=[2,3,4,5,6]
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
        print(sum)
sum()
    