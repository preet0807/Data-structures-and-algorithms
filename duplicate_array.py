n= int(input("enter the size of your array"))
lst=[]
for i in range(0,n):
    m=int(input("please enter the elements of the array"))
    lst.append(m)
c=0
for a in lst:
    n=lst.count(a)
    c=c+1;

if c>0:
    
         print("true")
else:
        print("false")
    

