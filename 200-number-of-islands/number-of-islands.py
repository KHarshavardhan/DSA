class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        count=0
        def dfs(r,c):
            if (r<0 or c<0 or r>=row or c>=col or (r,c) in visit or grid[r][c]=='0'):
                return False
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return True
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and (r,c) not in visit:
                    dfs(r,c)
                    count+=1
        return count