class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]]=i
        step=1
        end=0
        res=[]
        for j in range(len(s)):
            if hashmap[s[j]]>end:
                end=hashmap[s[j]]
            if j==end:
                res.append(step)
                step=0
            step+=1
        print(hashmap)
        return(res)