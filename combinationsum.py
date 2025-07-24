def generate(ind,curr,ans,candidates,target):
    if(target==0):
        ans.append(curr.copy())
        return
    if(target<0 or ind==len(candidates)):
        return
    curr.append(candidates[ind])
    generate(ind,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    generate(ind+1,curr,ans,candidates,target)
def combinationsSum(candidates,target):
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
candidates=[2,3,6,7]
target=7
print(combinationsSum(candidates,target))
           