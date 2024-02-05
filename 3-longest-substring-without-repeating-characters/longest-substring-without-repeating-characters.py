class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newstr = set()
        leftpointer = 0
        count = 0
        for i in range(len(s)):
            while s[i] in newstr:
                newstr.remove(s[leftpointer])
                leftpointer +=1
            newstr.add(s[i])
            count=max(count,i-leftpointer + 1)
        return count

            
        