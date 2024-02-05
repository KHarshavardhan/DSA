class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for i in s:
            if i.isalnum():
                newstr += i.lower()
        # if newstr[::-1] == newstr:
        #     return True
        # else:
        #     return False
        if len(newstr)>0:
            for i in range(len(newstr)):
                j = len(newstr)-i-1
                if i>=j:
                    return True
                if newstr[i] != newstr[j] or i>=j:
                    break
                else:
                    continue
            return False
        else:
            return True