# def table():
#   num=int(input("enter the number"))
#   i=0
#   while i<=10:
#     if num<0:
#        print("number")
#     else:
#        print(num,"*",1,"=",num*1)
#        print(num,"*",2,"=",num*2)
#        print(num,"*",3,"=",num*3)
#        print(num,"*",4,"=",num*4)
#        print(num,"*",5,"=",num*5)
#        print(num,"*",6,"=",num*6)
#        print(num,"*",7,"=",num*7)
#        print(num,"*",8,"=",num*8)
#        print(num,"*",9,"=",num*9)
#        print(num,"*",10,"=",num*10)
#        i=i+1
# table()

def table():
    a=int(input("enter the number"))
    i=1
    while i<=10:
        table=a*i
        print(a,"*",i,"=",table)
        i=i+1
table()
    
