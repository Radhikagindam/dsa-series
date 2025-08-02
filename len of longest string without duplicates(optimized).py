def len_of_longest_string(s):
    n=len(s)
    maxlen=0
    left=0
    right=0
    d={}
    while(right<n):
        if(s[right] in d):
            if(d[s[right]]>=left):
                left=d[s[right]]+1
        d[s[right]]=right
        maxlen=max(maxlen,right-left+1)
        right+=1
    return maxlen
s=input() #cadbzabcd
print(len_of_longest_string(s))
