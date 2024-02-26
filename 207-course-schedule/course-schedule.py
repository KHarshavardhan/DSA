class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i:[] for i in range(numCourses)}
        visit=set()
        for c in prerequisites:
            pre[c[0]].append(c[1])
        def dfs(crs):
            if crs in visit:
                return False
            if pre[crs]==[]:
                return True
            visit.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            visit.remove(crs)
            pre[crs]=[]
            return True
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True