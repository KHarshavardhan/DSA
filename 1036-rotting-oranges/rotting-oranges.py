class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque()
        time,fresh=0,0
        #step1: get the count of fresh oranges and also append rotten oranges into deque
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
        #step2: loop through queue untill either fresh oranges are over or q is empty
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh >0:
            #step2_1:range(len(q)) locks the current rotten oranges count and goes through them
            for i in range(len(q)):
                #step2_2:for each rotten orange go through all 4 directions and if fresh orange found-->rotten and add rotten into queue
                r,c=q.popleft()
                for dr,dc in directions:
                    if (r+dr<0 or c+dc<0 or r+dr>=row or c+dc>=col or grid[r+dr][c+dc]!=1):
                        continue
                    grid[r+dr][c+dc]=2
                    q.append([r+dr,c+dc])
                    fresh-=1
            #step2_3:For every batch of rotten oranges, time unit is incremented
            time+=1
        return time if fresh<=0 else -1
        