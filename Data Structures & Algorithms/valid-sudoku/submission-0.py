class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                row_entry = ("row", r, val)
                col_entry = ("col", c, val)
                box_entry = ("box", (r // 3) * 3 + (c // 3), val)

                if (row_entry in seen) or (col_entry in seen) or (box_entry in seen):
                    return False
                
                seen.add(row_entry)
                seen.add(col_entry)
                seen.add(box_entry)

        return True