class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        for i in range(2**l):
            temp = []
            for j in range(l):
                if i>>j&1:
                    temp.append(nums[j])
            res.append(temp)
        return res
