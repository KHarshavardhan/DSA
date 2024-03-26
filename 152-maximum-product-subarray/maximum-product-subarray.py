class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cMin,cMax=1,1
        for n in nums:
            temp=cMax
            cMax=max(cMax*n,cMin*n,n)
            cMin=min(temp*n,cMin*n,n)
            res=max(res,cMax,cMin)
        return res