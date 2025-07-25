def generate(ind,ans,curr,candidates,target):
    if(target==0):
        ans.append(curr.copy())
        return
    if(target<0 or ind==len(candidates)):
        return
    curr.append(candidates[ind])
    generate(ind,curr,ans,target-candidates,candidates)
    curr.pop()
    generate(ind+1,curr,ans,candidates,target)
def combinationssum(candidates:list[int],target:[int]):
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
print(ans)
           
