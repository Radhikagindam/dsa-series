arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
maxlen=0
for i in range(0,n):
    for j in range(i,n):
        if(sum(arr[i:j+1])<=k):
            maxlen=max(maxlen,j-i+1)
print(maxlen)