class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(s,i):
            if sum(s)==target:
                res.append(s.copy())
                return
            if sum(s)>target or i>=len(candidates):
                return
            s.append(candidates[i])
            backtracking(s,i)
            s.pop()
            backtracking(s,i+1)
        backtracking([],0)
        return res