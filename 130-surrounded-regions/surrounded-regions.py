class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        visit=set()

        def dfs(r,c):
            if r<0 or c<0 or r==row or c==col or board[r][c]!='O' or (r,c) in visit:
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(row):
            for c in range(col):
                if (board[r][c]=='O' and (r in [0,row-1] or c in [0,col-1])):
                    dfs(r,c)
        for r in range(row):
            for c in range(col):
                if (board[r][c]=='O'):
                    board[r][c]='X'
                if (board[r][c]=='T'):
                    board[r][c]='O'

        
        
        