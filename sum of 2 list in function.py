def sum():
  a=[50, 60, 10] 
  b=[10, 20, 13]
  i=0
  c=[]
  while(i<len(a)):
        while(i<len(b)):
              c.append(a[i]+b[i])
              i=i+1
        i=i+1      
  print(c)            
sum()