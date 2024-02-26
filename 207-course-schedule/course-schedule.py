class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #pre is a hashmap to store cources based on index,here creating a empty hashmap
        pre = {i:[] for i in range(numCourses)}
        visit=set()
        #adding all courses into hashmap
        for c in prerequisites:
            pre[c[0]].append(c[1])
        #dfs will take course value and checks,wheather it is creating a loop, if yes then return false else adds to the visit set, also a hashmap key can have mutiple course as prereq, so it goes through all.
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
        #last stage to check all indexes and run dfs on all, if nothing return false, i.e it can be completed, hence true is returned
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True