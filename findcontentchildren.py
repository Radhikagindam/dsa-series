def findcontentchildren(g:list[int]):
    g.sort()
    s.sort()
    left=0
    right=0
    n=len(s)
    m=len(g)
    while(left<n and right<m):
        if(s[left]>=g[right]):
            left+=1
            right+=1
        else:
            left+=1
    return right