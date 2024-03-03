class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        visitp =[]
        visita=[]
        res=[]
        #check if water can pass from pacific to how many cells as possible(if current value is less than next value) and add them into visitp. same in atlantic add to visita
        def dfs(r,c,visit,temp):
            if(r<0 or c<0 or r>=row or c>=col or [r,c] in visit or heights[r][c]<temp):
                return
            temp=heights[r][c]
            visit.append([r,c])
            dfs(r+1,c,visit,temp)
            dfs(r-1,c,visit,temp)
            dfs(r,c+1,visit,temp)
            dfs(r,c-1,visit,temp)
        for i in range(row):
            if i==0:
                for j in range(col):
                    dfs(i,j,visitp,heights[i][j])
            else:
                dfs(i,0,visitp,heights[i][0])
        for k in range(col):
            if k==col-1:
                for j in range(row):
                    dfs(j,k,visita,heights[j][k])
            else:
                dfs(row-1,k,visita,heights[row-1][k])
        #once the two lisit is created with cells which has pacific water and atlantic separte then check for common cells and return them.
        for rp,cp in visitp:
            if [rp,cp] in visita:
                res.append([rp,cp])
        return res
        