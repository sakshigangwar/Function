def speeed(a):
    if a<=70:
        print("70")
    elif a>70:
        n=(a-70)//5
        if n<12:
            print(n)
        else:
            print("license suspended")
a=int(input("enter the number"))
speeed(a)
        




