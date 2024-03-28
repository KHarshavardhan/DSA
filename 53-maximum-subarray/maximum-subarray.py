class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        curSum=0
        res=float("-infinity")
        for n in nums:
            if curSum<=0:
                curSum=0
            curSum+=n
            res=max(res,curSum)
        return res