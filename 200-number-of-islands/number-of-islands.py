class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid),len(grid[0])
        visit = set()
        noIsland= 0
        #breath for search is not recursive, its iterative and goes through all possiblilities and adds them to visit set
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r,c=q.popleft()
                direct = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in direct:
                    if ((r+dr) in range(row) and (c+dc) in range(col) and grid[r+dr][c+dc] == '1' and (r+dr,c+dc) not in visit):
                        visit.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))
        #once deque is empty, that means one island is completed
        #now entire collection of 1s is considered as one island and moves forward
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and (r,c) not in visit:
                    bfs(r,c)
                    noIsland+=1
        return noIsland