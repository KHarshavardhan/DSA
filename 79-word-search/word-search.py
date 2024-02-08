class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visit = set()
        def backtracking(r,c,i):
            if i == len(word):
                return True
            if r>=row or c>=col or ((r,c) in visit) or word[i]!=board[r][c] or r<0 or c<0:
                return False
            visit.add((r,c))
            res = (backtracking(r+1,c,i+1) or
            backtracking(r-1,c,i+1) or
            backtracking(r,c+1,i+1) or
            backtracking(r,c-1,i+1) )
            visit.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                if backtracking(r,c,0):
                    return True
        return False
        