class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        res=float("-infinity")
        tsum=0
        for i in nums:
            if tsum<0:
                tsum=0
            tsum+=i
            res=max(res,tsum)
        return res
