def a():
    num=int(input("enter the number"))  
    i=num
    sum=0
    while i>0:
        sum=sum+(i%10)*(i%10)*(i%10)
        i=i//10
    if num==sum:
        print("armstrong")
    else:
        print("not armstrong")
a()


