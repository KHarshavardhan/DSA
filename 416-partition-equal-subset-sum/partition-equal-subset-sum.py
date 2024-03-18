class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = set()
        s.add(0)
        res=0 
        if sum(nums)%2==0:
            res=sum(nums)//2 
        else:
            return False 
        
        for n in nums[::-1]:
            for i in s.copy():
                s.add(i+n)
                if res in s:
                    print(s)
                    return True
        print(s)
        return False
