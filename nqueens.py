import time

class NQueensBacktracking:
    """Solves the N-Queens problem using backtracking"""
    
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.calls = 0
    
    def is_safe(self, board, row, col):
        """Check if a queen can be placed at board[row][col]"""
        self.calls += 1
        
        # Check row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve_util(self, board, col):
        """Recursive utility function for backtracking"""
        # Base case: If all queens are placed
        if col >= self.n:
            solution = []
            for i in range(self.n):
                row = []
                for j in range(self.n):
                    row.append(board[i][j])
                solution.append(row)
            self.solutions.append(solution)
            return True
        
        res = False
        # Try placing queen in each row of this column
        for row in range(self.n):
            if self.is_safe(board, row, col):
                # Place the queen
                board[row][col] = 1
                
                # Recur to place rest of the queens
                res = self.solve_util(board, col + 1) or res
                
                # Backtrack and remove the queen
                board[row][col] = 0
        
        return res
    
    def solve(self):
        """Solve the N-Queens problem"""
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        start_time = time.time()
        self.solve_util(board, 0)
        end_time = time.time()
        
        return len(self.solutions), self.calls, end_time - start_time


class NQueensBranchAndBound:
    """Solves the N-Queens problem using Branch and Bound"""
    
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.calls = 0
        # Arrays to track occupied diagonals and columns
        self.left_diagonal = [0] * (2 * n - 1)
        self.right_diagonal = [0] * (2 * n - 1)
        self.cols = [0] * n
    
    def is_safe(self, row, col):
        """Check if queen can be placed using Branch and Bound"""
        self.calls += 1
        # Check if no queen occupies the column or diagonals
        if (self.cols[col] or 
            self.left_diagonal[row + col] or 
            self.right_diagonal[row - col + self.n - 1]):
            return False
        return True
    
    def solve_util(self, board, row):
        """Recursive utility function with Branch and Bound"""
        # Base case: If all queens are placed
        if row >= self.n:
            solution = []
            for i in range(self.n):
                row_list = []
                for j in range(self.n):
                    row_list.append(board[i][j])
                solution.append(row_list)
            self.solutions.append(solution)
            return True
        
        res = False
        # Try placing queen in each column of this row
        for col in range(self.n):
            if self.is_safe(row, col):
                # Place queen and mark occupied paths
                board[row][col] = 1
                self.cols[col] = 1
                self.left_diagonal[row + col] = 1
                self.right_diagonal[row - col + self.n - 1] = 1
                
                # Recur to place rest of the queens
                res = self.solve_util(board, row + 1) or res
                
                # Backtrack
                board[row][col] = 0
                self.cols[col] = 0
                self.left_diagonal[row + col] = 0
                self.right_diagonal[row - col + self.n - 1] = 0
        
        return res
    
    def solve(self):
        """Solve the N-Queens problem"""
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        start_time = time.time()
        self.solve_util(board, 0)
        end_time = time.time()
        
        return len(self.solutions), self.calls, end_time - start_time


def print_solution(solution):
    """Print a solution of the N-Queens problem"""
    for row in solution:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()


if __name__ == "__main__":
    # Get board size from user
    n = int(input("Enter the size of the board (n): "))
    
    print("\n=== Solving with Backtracking ===")
    backtracking = NQueensBacktracking(n)
    solutions, calls, time_taken = backtracking.solve()
    print(f"Found {solutions} solutions in {time_taken:.6f} seconds with {calls} function calls")
    
    if solutions > 0:
        print("\nFirst solution:")
        print_solution(backtracking.solutions[0])
    
    print("\n=== Solving with Branch and Bound ===")
    branch_bound = NQueensBranchAndBound(n)
    solutions, calls, time_taken = branch_bound.solve()
    print(f"Found {solutions} solutions in {time_taken:.6f} seconds with {calls} function calls")
    
    if solutions > 0:
        print("\nFirst solution:")
        print_solution(branch_bound.solutions[0])