class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(curr,o,c):
            if o==n and c==n:
                res.append(curr)
                return
            o=curr.count('(')
            if o<n:
                backtracking(curr+'(',o,c)
            if c<o:
                backtracking(curr+')',o,c+1)
            
        backtracking("",0,0)
        return res
