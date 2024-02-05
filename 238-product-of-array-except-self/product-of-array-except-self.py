import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfElements = math.prod(nums)
        result=[]
        muti = 1
        if productOfElements != 0:
            for i in nums:
                result.append(productOfElements//i)
        elif nums.count(0) == 1:
            newNums = [ i for i in nums if i!=0]
            productOfNonZeros = math.prod(newNums)
            for i in nums:
                if i != 0:
                    muti *= i
                    result.append(0)
                else:
                    result.append(productOfNonZeros)
        else:
            result = [0]*len(nums)
        return result
        