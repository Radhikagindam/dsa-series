def longestones(nums,k):
    n=len(nums)
    left=0
    right=0
    maxlen=0
    count_zeros=0
    while(right<n):
        if(nums[right]==0):
            count_zeros+=1
        if(count_zeros>k):
            while(count_zeros>k):
                if(nums[left]==0):
                    count_zeros-=1
                left+=1
        maxlen=max(maxlen,right-left+1)
        right+=1
    return maxlen
nums=list(map(int,input().split()))
k=int(input())
print(longestones(nums,k))