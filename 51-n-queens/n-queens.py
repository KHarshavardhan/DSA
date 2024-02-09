class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        col = set()
        posDiag = set() #(r-c)
        negDiag = set() #(r+c)
        board = [['.']*n for i in range(n)]
        def backtracking(r):
            if r==n:
                temp = ["".join(row) for row in board]
                res.append(temp)
                return
            for c in range(n):
                if c in col or (r+c) in negDiag or (r-c) in posDiag:
                    continue 
                col.add(c)
                negDiag.add(r+c)
                posDiag.add(r-c)
                board[r][c]="Q"
                backtracking(r+1)
                col.remove(c)
                negDiag.remove(r+c)
                posDiag.remove(r-c)
                board[r][c]="."
        backtracking(0)
        return res
                