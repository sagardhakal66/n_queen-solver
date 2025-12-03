def solve_n_queens(n):
    solutions = []
    
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1
        
        return True
    
    def backtrack(board, col):
        if col >= n:
            solution = []
            for i in range(n):
                row_str = ""
                for j in range(n):
                    row_str += "Q" if board[i][j] == 1 else "."
                solution.append(row_str)
            solutions.append(solution)
            return
        
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, col + 1)
                board[row][col] = 0
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    
    return solutions
