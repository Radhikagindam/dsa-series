def funbc(fruits):
    n=len(fruits)
    maxlen=0
    for i in range(0,n):
        s=set() #to declare an empty set
        for j in range(i,n):
            s.add(fruits[j])
            if(len(s)>2):
                break
            maxlen=max(maxlen,j-i+1)
    return maxlen
fruits=list(map(int,input().split()))
print(funbc(fruits))
