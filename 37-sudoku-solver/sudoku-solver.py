class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize the structures to track availability of numbers
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        subbox = [[False] * 9 for _ in range(9)]
        
        # Fill in the tracking structures based on the initial board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    d = int(board[r][c]) - 1
                    row[r][d] = col[c][d] = subbox[(r//3)*3 + c//3][d] = True
        
        def isValid(r, c, d):
            """
            Check if d can be placed at board[r][c]
            """
            return not (row[r][d] or col[c][d] or subbox[(r//3)*3 + c//3][d])
        
        def placeNumber(r, c, d):
            """
            Place d at board[r][c] and update tracking structures
            """
            board[r][c] = str(d + 1)
            row[r][d] = col[c][d] = subbox[(r//3)*3 + c//3][d] = True
        
        def removeNumber(r, c, d):
            """
            Remove d from board[r][c] and update tracking structures
            """
            board[r][c] = '.'
            row[r][d] = col[c][d] = subbox[(r//3)*3 + c//3][d] = False
        
        def backtrack(r=0, c=0):
            """
            Backtrack from board[r][c] forward
            """
            if r == 9:
                return True  # Puzzle solved
            if board[r][c] != '.':
                return backtrack(r + (c + 1) // 9, (c + 1) % 9)
            for d in range(9):
                if isValid(r, c, d):
                    placeNumber(r, c, d)
                    if backtrack(r + (c + 1) // 9, (c + 1) % 9):
                        return True
                    removeNumber(r, c, d)
            return False
        
        backtrack()
