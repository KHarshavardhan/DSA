class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            row , col = len(matrix),len(matrix[0])
            top , btm = 0,row*col-1
            while top<=btm:
                mid = (top+btm)//2
                r = mid // col
                c = mid % col
                if matrix[r][c] == target:
                    return True
                elif target > matrix[r][c]:
                    top = mid+1
                else:
                    btm = mid -1
            return False
