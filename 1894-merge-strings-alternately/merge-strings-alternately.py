class Solution(object):
    def mergeAlternately(self, word1, word2):
        r=""
        l1=len(word1)
        l2=len(word2)
        s=min(l1,l2)
        for i in range(s):
            r+=word1[i]+word2[i]
        if l1>l2:
            r+=word1[i+1:]
        elif l1<l2:
            r+=word2[i+1:]
        return r

        
        

        
        
        

        