class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_count=[set() for _ in range(9)]
        column_count=[set() for _ in range(9)]
        box_count=[set() for _ in range(9)]

        for i in range(len(board)):
            
            for j in range(len(board[i])):

                value=board[i][j]
                
                if board[i][j]=='.':
                    continue

                box_index=(i//3)*3+(j//3)
                if (
                    value in row_count[i] or 
                    value in column_count[j] or
                    value in box_count[box_index]
                ):
                    return False

                row_count[i].add(value)
                column_count[j].add(value)
                box_count[box_index].add(value)

        return True

                
        