class Solution:
    def rob(self, nums: List[int]) -> int:
        #need to run the house robber 1 sol twice for two subsets
        if len(nums)==1:
            return nums[0]
        else:
            r1,r2,ans1,ans2=0,0,0,0
            num=nums[:-1]
            for n in num:
                temp=max(r1+n,r2)
                r1=r2
                r2=temp
            ans1=r2
            r1,r2=0,0
            num=nums[1:]
            for n in num:
                temp=max(r1+n,r2)
                r1=r2
                r2=temp
            ans2=r2
            return max(ans1,ans2)