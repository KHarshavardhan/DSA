class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        PostDiag = set() #(r-c)
        NegDiag = set() #(r+c)

        board = [["."]*n for i in range(n)]
        def backtracking(r):
            if r == n:
                temp = ["".join(row) for row in board]
                res.append(temp)
                return
            for c in range(n):
                if c in col or (r-c) in PostDiag or (r+c) in NegDiag :
                    continue
                col.add(c)
                PostDiag.add(r-c)
                NegDiag.add(r+c)
                board[r][c] = "Q"
                backtracking(r+1)
                col.remove(c)
                PostDiag.remove(r-c)
                NegDiag.remove(r+c)
                board[r][c] = "."
        backtracking(0)
        return res