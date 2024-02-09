class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n=len(s)
        if n==0:
            return [[]]
        for i in range(1,n+1):
            if s[:i]==s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    res.append([s[:i]]+suf)
        return res