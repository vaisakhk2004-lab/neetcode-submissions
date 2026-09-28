class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for col in range(len(cols)):
            for row in range(len(rows)):
                number=board[row][col]
                if  number=='.':
                    continue
                if number in rows[row] or number in cols[col] or number in boxes[row//3][col//3]:
                    return False
                rows[row].add(number)
                cols[col].add(number)
                boxes[row//3][col//3].add(number)
        return True

        