# def prime(a):
#     count=0
#     i=1
#     while i<=a:
#         if a%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         print("prime number")
#     else:
#         print("not prime number")
#         i=i+1
# prime()


def prime(num):
        if num>1:
         for i in range (2,num):
            if (num%i)==0:
                print(num,"is not prime number")
                print(i,"time",num//i,"is",num)
                break
            else:
                print(num,"is prime number")
        else:
          print(num,"is not prime number")
prime(406)