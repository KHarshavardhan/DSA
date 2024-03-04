class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque()
        fresh=0
        timer=0
        visit=set()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
            d = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in d:
                    rr,cc=r+dr,c+dc
                    if(rr in range(row) and cc in range(col) and (rr,cc) not in visit and grid[rr][cc]==1):
                        grid[rr][cc]=2
                        q.append((rr,cc))
                        visit.add((rr,cc))
                        fresh-=1
            timer+=1
        return timer if fresh<=0 else -1  
