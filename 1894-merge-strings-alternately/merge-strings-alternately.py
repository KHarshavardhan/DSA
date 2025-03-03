class Solution(object):
    def mergeAlternately(self, word1, word2):
        r=""
        s=min(len(word1),len(word2))
        for i in range(s):
            r+=word1[i]
            r+=word2[i]
        if len(word1)>len(word2):
            r+=word1[i+1:]
        elif len(word1)<len(word2):
            r+=word2[i+1:]
        return r

        
        

        
        
        

        