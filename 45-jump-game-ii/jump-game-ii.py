class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        r,l=0,0
        while r<len(nums)-1:
            far = 0
            for i in range(l,r+1):
                far = max(far,i+nums[i])
            l=r+1
            r=far
            ans+=1
        return ans