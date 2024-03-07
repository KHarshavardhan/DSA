class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        else:
            res=0
            one = 1
            two = 1
            while n>1:
                res=one+two
                temp=one
                one=res
                two=temp
                n-=1
            return res

