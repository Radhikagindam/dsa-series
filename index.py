def findmin(arr):
    low=0
    high=len(arr)-1
    min=float("inf")
    ind=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<=min):
                min=arr[low]
                ind=low
            low=mid+1
        elif(arr[mid]<=arr[high]): 
            if(arr[mid]<=min):
                min=arr[mid]
                ind=mid
            high=mid-1
    return ind
arr=list(map(int,input().split()))
print(findmin(arr))
