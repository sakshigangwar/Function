# def sum(number):
#     if number==1:
#         return 1
#     return 2 * sum(number-1)

# index=1
# while(index<10):
#     print(sum(index))
#     index+=1




# def pattern(number):
#     if number == 1:
#         return 1
#     else:
#         return pattern(number-1) + 3
# index=1
# while(index<10):
#     print(pattern(index))
#     index+=1

# def pattern(number):
#     if number == 1:
#         return 10
#     elif number % 2 == 0:
#         return pattern(number - 1) + 1
#     else:
#         return pattern(number - 1) * 10
# index=1
# while(index<10):
#     print(pattern(index))
#     index+=1


# def factorial(number):
#     if number==1:
#         return 1
#     return number * factorial(number - 1)

# print (factorial(5))





# i=4                ****
# while i>=1:        ***
#     print( i*"*")  **
#     i=i-1          *
# i=0                *
# while i<=4:        **
#     print(i*"*")   ***
#     i=i+1          ****

# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0] + sum_list(lis[1:])

# print (sum_list([1, 4, 7, 10]))


# def ifPalindrome(string):
#     if string == "":  # BASE CASE CONDITION
#         return True
#     elif len(string) == 1:  # BASE CASE CONDITION
#         return True
#     elif string[0] == string[len(string)-1]:  # RECURSION
#         return ifPalindrome(string[1:][:-1])
#     else:
#         return False
# print(ifPalindrome(input("enter the stringg:")))

# def getFibNumber(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return getFibNumber(number-1) + getFibNumber(number-2)
# getFiNumner()



# def fib(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return fib(number-1) + fib(number-2)

# def getFibList(number):
#     fib_list = []
#     key = 1
#     while (key < number + 1):
#         fib_list.append(fib(key))
#         key += 1
#     return fib_list

# print(getFibList(10))

# def operate(num1, operator, num2):
#     if operator=='+':
#         return num1 + num2
#     elif operator=='-':
#         return num1 - num2
#     elif operator=='*':
#         return num1 * num2
#     else:
#         return num1 / num2
# print(operate(input("enter the number")))




# n=int(input("Enter the number"))
# b=n-100
# if n<100:
#     print("free")
# elif 100<=n and 200>=n:
#     a=b*5
#     print(a)
# else:
#     print(n-(n-100)*5+(n-200)*10)


    
# a=[[1,23,],[2,3,4,5],[4,5,6,7,8]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[j])<len(a[i]):
#         j=j+1
#     i=i+1
# print("max lenth=",len(a[j]),a[j])


# def name(a=input("enter the name")):
#     n=int(input("enter the number"))
#     i=0
#     while i<len(a):
#         i=i+1
#     print(n*a)
# name()

# n=int(input("enter the number"))
# i=n
# while i>0:
#     i=i-1
#     print(i,end="")

