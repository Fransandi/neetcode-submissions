class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(9):
            seen = set()
            for n in board[row]:
                if n != '.' and n in seen:
                    return False
                seen.add(n)

        # Check cols
        for col in range(9):
            seen = set()
            for row in range(9):
                n = board[row][col]
                if n != '.' and n in seen:
                    return False
                seen.add(n)

        # Check quadrants
        for q1_s in [0, 3, 6]:
            for q2_s in [0, 3, 6]:
                seen = set()
                for q1 in range(3):
                    for q2 in range(3):
                        n = board[q1_s + q1][q2_s + q2] 
                        if n != '.' and n in seen:
                            return False
                        seen.add(n)

        return True

            
        