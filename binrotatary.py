def search(arr,key):
    low=0
    high=len(arr-1)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        if(arr[low]<=arr[mid]):
            high=mid-1
        else:
            low=mid+1
    elif(arr[mid]<=arr[high]):
        if(arr[mid]<=key<=arr[high]):
            low=mid+1
        else:
            high=mid-1
    return -1
arr=list(map(int,input().split()))
key=int(input())
print(search(arr,key))