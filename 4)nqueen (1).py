class NQueen:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n   # board[row] = column position of queen
        self.solutions = []

    def is_safe(self, row, col):
        for prev_row in range(row):
            prev_col = self.board[prev_row]

            # Check column conflict
            if prev_col == col:
                return False

            # Check diagonal conflict
            if abs(prev_col - col) == abs(prev_row - row):
                return False

        return True

    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve(row + 1)
                self.board[row] = -1  # backtrack

    def display(self, solution):
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if solution[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


if __name__ == "__main__":
    n = 4
    problem = NQueen(n)
    problem.solve()

    print(f"Total Solutions for {n}-Queens:", len(problem.solutions))

    for sol in problem.solutions:
        problem.display(sol)

