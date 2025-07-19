def isanagram(s:str,t:str)->bool:
    return sorted(s)==sorted(t)
print(isanagram("listen", "silent"))
