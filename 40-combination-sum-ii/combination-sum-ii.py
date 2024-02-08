class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(pos,total,cur):
            if total==0:
                res.append(cur.copy())
                return
            if total<=0:
                return
            prev = -1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtracking(i+1,total-candidates[i],cur)
                cur.pop()
                prev = candidates[i]
        backtracking(0,target,[])
        return res