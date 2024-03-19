class Solution:
    def climbStairs(self, n: int) -> int:
        res=[0]
        dp=[-1]*(n*2)
        def f(m):
            if m>n:
                return 0
            if m==n:
                # res[0]+=1
                return 1
            if dp[m]!=-1:
                return dp[m]
            dp[m]=f(m+1)+f(m+2)
            return dp[m]
        return f(0) 