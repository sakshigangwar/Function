def reverse():
    list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    i=len(list)-1
    b=[]
    while i>=0:
        b.append(list[i])
        i=i-1
    print(b)
reverse()