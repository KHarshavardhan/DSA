class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        cmin,cmax=0,0
        res=float("-inf")
        for n in nums:
            temp=cmax
            cmax=max(cmax+n,cmin+n,n)
            cmin=min(temp+n,cmin+n,n)
            res = max(res,cmax,cmin)
        return res