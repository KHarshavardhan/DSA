class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre={i:[] for i in range(numCourses)}
        visit=set()
        res=[]
        for c,p in prerequisites:
            pre[c].append(p)
        def dfs(crs):
            if crs in visit:
                return False
            if pre[crs]==[]:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            if crs not in res:
                    res.append(crs)
            visit.remove(crs)
            pre[crs]=[]
            return True
        for x in range(numCourses):
            if not dfs(x):
                return []
        return res