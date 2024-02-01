class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            sub = []
            b = list(bin(i)[2:]) 
            count = 0
            for x in b[::-1]:
                if x == '1':
                    sub.append(nums[count])
                count+=1
            sub.sort()
            if sub not in ans:
                ans.append(sub)
        return ans