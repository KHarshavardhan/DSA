class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque()
        time,fresh=0,0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh >0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    if (r+dr<0 or c+dc<0 or r+dr>=row or c+dc>=col or grid[r+dr][c+dc]!=1):
                        continue
                    grid[r+dr][c+dc]=2
                    q.append([r+dr,c+dc])
                    fresh-=1
            time+=1
        return time if fresh<=0 else -1
        