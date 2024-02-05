class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # length = len(nums)
        # for i in range(length):
        #     temp=nums[i]
        #     del(nums[i])
        #     #nums.remove(temp)
        #     if temp in nums:
        #         return True
        #     else:
        #         nums.insert(i,temp)
        # return False
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
            
