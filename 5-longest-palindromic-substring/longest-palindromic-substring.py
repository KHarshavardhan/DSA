class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        length = 0
        def pal(l,r):
            nonlocal length
            nonlocal result
            while l >=0 and r <len(s) and s[l]==s[r]:
                if (r-l+1)>length:
                    length = r-l+1
                    result = s[l:r+1]
                    #print(result)
                l-=1
                r+=1
        for i in range(len(s)):
            l,r = i,i
            pal(l,r)
            l,r=i,i+1
            pal(l,r)
        return result