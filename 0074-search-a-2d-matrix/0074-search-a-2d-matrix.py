class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        t = row * column
        l = 0
        r = t -1 
        #doing this because we need to work on flattened version of array
        while l<=r:
            row = (l +r) //2
            i = row // column
            j= row % column
            midnum = matrix[i][j]
            if target == midnum:
                return True
            elif target < midnum:
                r = row-1
            else: 
                l = row +1
        return False
