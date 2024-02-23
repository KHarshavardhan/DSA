class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        p,a=set(),set()

        def dfs(r,c,visit,prev):
            if ((r,c) in visit or r<0 or c<0 or r==row or c==col or heights[r][c]<prev):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for c in range(col):
            dfs(0,c,p,heights[0][c])
            dfs(row-1,c,a,heights[row-1][c])
        
        for r in range(row):
            dfs(r,0,p,heights[r][0])
            dfs(r,col-1,a,heights[r][c])
        res= []
        for r in range(row):
            for c in range(col):
                if (r,c) in p and (r,c) in a:
                    res.append([r,c])
        return res