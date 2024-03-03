class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        res=[]
        def dfs(r,c):
            if (r<0 or c<0 or r>=row or c>=col or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return(1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (r,c) not in visit:
                    res.append(dfs(r,c))
        return max(res) if res else 0