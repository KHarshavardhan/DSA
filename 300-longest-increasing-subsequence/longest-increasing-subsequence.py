class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        for n in nums:
            bs = bisect_left(temp,n)
            if bs==len(temp):
                temp.append(n)
            elif temp[bs]>n:
                temp[bs]=n
        return len(temp)
