

class Fukoshiki():

    # Fukoshiki class contains the filename, size of the puzzle, the puzzle matrix and the row and column constraints
    def __init__(self, input_file):
        self.input_file = input_file
        self.num_cells = 5
        self.matrix = []
        self.row_constraints = []
        self.col_constraints = []
        self.get_matrix(input_file)

    # Reads from the input file to get the puzzle matrix and row/column constraints
    def get_matrix(self, filename):
        with open(filename, 'r') as file:
            for i in range(self.num_cells):
                str_row = file.readline().strip().split()
                int_row = [int(num) for num in str_row]
                self.matrix.append(int_row)
            file.readline()

            for i in range(self.num_cells):
                row = file.readline().strip().split()
                self.row_constraints.append(row)
            file.readline()

            for i in range(self.num_cells-1):
                row = file.readline().strip().split()
                self.col_constraints.append(row)

    # Checks if value alreadu in the row
    def allowed_in_row(self, val, row):
        for num in self.matrix[row]:
            if num == val:
                return False
        return True

    # Checks if value already in column
    def allowed_in_col(self, val, col):
        for row in range(self.num_cells):
            if self.matrix[row][col] == val:
                return False
        return True

    # Verifies that a certain poistion and value is allowed by constraints
    def satisfies_constraints(self, val, row_num, col_num):
        if col_num > 0:
            if (self.row_constraints[row_num][col_num - 1] == '>' and self.matrix[row_num][col_num - 1] != 0 and
            self.matrix[row_num][col_num - 1] < val):
                return False
            elif (self.row_constraints[row_num][col_num - 1] == '<' and self.matrix[row_num][col_num - 1] != 0 and
            self.matrix[row_num][col_num - 1] > val):
                return False

        if col_num < self.num_cells - 1:
            if (self.row_constraints[row_num][col_num] == '>' and self.matrix[row_num][col_num + 1] != 0 and
            val < self.matrix[row_num][col_num + 1]):
                return False
            elif (self.row_constraints[row_num][col_num] == '<' and self.matrix[row_num][col_num + 1] != 0 and
            val > self.matrix[row_num][col_num + 1]):
                return False

        if row_num > 0:
            if (self.col_constraints[row_num - 1][col_num] == 'v' and self.matrix[row_num - 1][col_num] != 0 and
            self.matrix[row_num - 1][col_num] < val):
                return False
            if (self.col_constraints[row_num - 1][col_num] == '^' and self.matrix[row_num - 1][col_num] != 0 and
            self.matrix[row_num - 1][col_num] > val):
                return False

        if row_num < self.num_cells - 1:
            if (self.col_constraints[row_num][col_num] == 'v' and self.matrix[row_num + 1][col_num] != 0 and
            val < self.matrix[row_num + 1][col_num]):
                return False
            if (self.col_constraints[row_num][col_num] == '^' and self.matrix[row_num + 1][col_num] != 0 and
            val > self.matrix[row_num + 1][col_num]):
                return False
        return True

    # Allows solving algorithm to proceed to the next cell without a value
    def get_empty_cell(self):
        for row in range(self.num_cells):
            for col in range(self.num_cells):
                if not self.matrix[row][col]:
                    return (row, col)
        return False

    def solve_puzzle(self):
        if not self.backtrack():
                print("Can't be solved")
        print(self.matrix)
        self.produce_output(self.matrix)
        return self.matrix

    # Visits empty cells to verify that they are noe empty and placing values
    def backtrack(self):
        cell = self.get_empty_cell()
        if not cell:
            return True

        for num in range(1, self.num_cells + 1):
            if (self.allowed_in_row(num, cell[0]) and self.allowed_in_col(num, cell[1]) and
            self.satisfies_constraints(num, cell[0], cell[1])):
                self.matrix[cell[0]][cell[1]] = num
                if self.backtrack():
                    return True
                self.matrix[cell[0]][cell[1]] = 0

        return False

    # Produces result output
    def produce_output(self, matrix):
        with open("Output" + self.input_file[5], 'w') as output_file:
            for row in matrix:
                for num in row:
                    output_file.write(str(num) + " ")
                output_file.write("\n")
