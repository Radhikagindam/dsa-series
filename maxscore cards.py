def maxscore(cardpoints,k):
    n=len(cardpoints)
    leftsum=sum(cardpoints[:k])
    maxsum=leftsum
    rightsum=0
    rightIndex = n-1
    for i in range(k-1,-1,-1):
        leftsum-=cardpoints[i]
        rightsum+=cardpoints[rightIndex]
        maxsum=max(maxsum,leftsum+rightsum)
        rightIndex-=1
    return maxsum
cardpoints=list(map(int,input().split()))#6 2 3 4 7 2 1 7 1
k=int(input())#4
print(maxscore(cardpoints,k))
