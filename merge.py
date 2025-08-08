def merge(num,low,high):
    if(low>=high):
        return
    mid=(low+high)//2
    merge(nums,low,mid)
    merge(nums,mid+1,high)
    sort(nums,low,mid,high)
def sort(nums,low,mid,high):
    i=low
    j=mid+1
    k=[]
    while(i<=mid and j<=high):
        if(nums[i]<=nums[j]):
            k.append(nums[i])
            i+=1
        else:
            k.append(nums[j])
            j+=1
    while(i<=mid):
        k.append(nums[i])
        i+=1
    while(j<=high):
         k.append(nums[j])
         j+=1
    for ind,val in enumerate(k):
        nums[low+ind]=val
nums=list(map(int,input().split()))
merge(nums,0,len(nums)-1)
print(nums)
    
         