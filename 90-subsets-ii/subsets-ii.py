class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**len(nums)):
            ans=[]
            for j in range(len(nums)):
                if i>>j & 1:
                    ans.append(nums[j])
            ans.sort()
            if ans not in res:
                res.append(ans)
        return res