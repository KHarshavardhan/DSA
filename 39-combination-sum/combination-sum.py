class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(s,i,total):
            if total==target:
                res.append(s.copy())
                return
            if total>target or i>=len(candidates):
                return
            s.append(candidates[i])
            backtracking(s,i,total+candidates[i])
            s.pop()
            backtracking(s,i+1,total)
        backtracking([],0,0)
        return res