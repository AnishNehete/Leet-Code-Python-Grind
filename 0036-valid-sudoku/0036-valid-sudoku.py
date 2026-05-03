class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen= set ()

        for r in range(9): #loop though
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                row_key = ('row', r, val) #create a unique key for this val
                col_key = ('col', c, val)
                box_key = ('box', r//3, c//3,val)

                if row_key in seen:
                    return False

                if col_key in seen:
                    return False

                if box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True

