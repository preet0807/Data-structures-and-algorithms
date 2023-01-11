num=[-2,1,-3,4,-1,2,1,-5,4]
n= len(num)
cur_sum=0
lst2=[]
max_sum=-1000000
for i in  range(0,n):
    cur_sum=cur_sum+num[i]
    if cur_sum>max_sum:
        max_sum=cur_sum
        lst2.append(num[i])
        
        
    if cur_sum<0:
        cur_sum=0
print(lst2)
print(max_sum)
    




