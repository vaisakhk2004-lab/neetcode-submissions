class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=[set() for _ in range(9)]
        columns=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                number=board[r][c]
                if number in rows[r]:
                    return False
                rows[r].add(number)
                if number in columns[c]:
                    return False
                columns[c].add(number)
                box=(r//3)*3+c//3
                if number in boxes[box]:
                    return False
                boxes[box].add(number)
        return True
        