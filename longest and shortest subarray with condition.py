arr=list(map(int,input().split()))# 2 3 5 8 10 12 3 1
k=int(input())#4
n=len(arr)
maxlen=0
for i in range(0,n):
    for j in range(i,n):
        if(len(arr[i:j+1])<=k):
            maxsum=max(maxlen,j-i+1)
print(maxlen) #35
        