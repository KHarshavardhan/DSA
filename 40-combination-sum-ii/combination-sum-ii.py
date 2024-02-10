class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        candidates.sort()
        def dfs(cur,pos,total):
            if total == 0:
                res.append(cur.copy())
                return
            if total<=0:
                return
            prev = -1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(cur,i+1,total-candidates[i])
                cur.pop()
                prev=candidates[i]
        dfs([],0,target)
        return res