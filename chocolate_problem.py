#we have to find the minimum and maximum difference between the elements of array of  size m 
# we will first sort the array

def minsubset(arr ,n ,m):
    if n==0 or m==0:
        return 0
     
    arr.sort()
    if n<m:
        return -1
    
    
    
    min_diff= arr[n-1]-arr[0]
    for i in range(0,n-m+1):
        d= arr[i+m-1]-arr[i]
        if d<min_diff:
            min_diff=d

    return min_diff

if __name__ == "__main__":
    arr=[7,3,2,4,9,12,56]
    m=3
    n=len(arr)
    print("minimum difference is ",minsubset(arr,n,m))

        