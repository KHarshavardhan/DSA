class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtracking(curr,pos,target):
            if target == 0:
                res.append(curr.copy())
                return
            if target<=0:
                return
            prev = -1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtracking(curr,i+1,target-candidates[i])
                curr.pop()
                prev= candidates[i]
        backtracking([],0,target)
        return res