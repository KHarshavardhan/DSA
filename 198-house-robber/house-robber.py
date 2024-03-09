class Solution:
    def rob(self, nums: List[int]) -> int:
        #[r1,r2,r3,...] this will nums list
        r1,r2=0,0
        #go through all nums and take max of r1+r3,r2
        for r3 in nums:
            c = max(r1+r3,r2)
            r1=r2
            r2=c
        #finally r2 which is final element will contain the max 
        return r2