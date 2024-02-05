class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        l = len(nums)
        while l>0:
            if nums[(left+right)//2] == target:
                return (left+right)//2
            else:
                if nums[(left+right)//2] > target:
                    right = ((left+right)//2)-1
                else:
                    left = ((left+right)//2)+1
            l /= 2
        return -1