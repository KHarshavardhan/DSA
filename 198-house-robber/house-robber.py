class Solution:
    def rob(self, nums: List[int]) -> int:
        r1,r2=0,0

        for r3 in nums:
            c = max(r1+r3,r2)
            r1=r2
            r2=c
        return r2