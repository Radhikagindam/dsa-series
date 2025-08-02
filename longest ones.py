#11100011110
def longestOnes(nums,k):
    n=len(nums)
    maxlen=0
    for i in range(0,n):
        zero_count=0
        for j in range(i,n):
            if(nums[j]==0):
                zero_count+=1
            if(zero_count>k):
                break
            maxlen=max(maxlen,j-i+1)
    return maxlen
nums=list(map(int,input().split()))
k=int(input())
print(longestOnes(nums,k))