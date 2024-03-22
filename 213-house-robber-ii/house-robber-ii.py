class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        r1,r2=0,0
        ans1,ans2=0,0
        for r in nums[:-1]:
            temp=max(r1+r,r2)
            r1=r2
            r2=temp
        ans1=r2
        r1,r2=0,0
        for r in nums[1:]:
            temp=max(r1+r,r2)
            r1=r2
            r2=temp
        ans2=r2
        return max(ans1,ans2)