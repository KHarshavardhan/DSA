class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #i have done this mult times 
        res= []
        def backtracking(arr,cur,total):
            if total==target:
                res.append(arr.copy())
                return
            if cur>=len(candidates) or total>=target:
                return
            arr.append(candidates[cur])
            backtracking(arr,cur,total+candidates[cur])
            arr.pop()
            backtracking(arr,cur+1,total)
        backtracking([],0,0)
        return res