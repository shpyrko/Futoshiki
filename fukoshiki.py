

class Fukoshiki():

    def __init__(self, input_file):
        self.num_cells = 4
        self.matrix = []
        self.row_constraints = []
        self.col_constraints = []
        self.get_matrix(input_file)


    def get_matrix(self, filename):
        with open(filename, 'r') as file:
            for i in range(self.num_cells+1):
                str_row = file.readline().strip().split()
                int_row = [int(num) for num in str_row]
                self.matrix.append(int_row)
            file.readline()

            for i in range(self.num_cells+1):
                row = file.readline().strip().split()
                self.row_constraints.append(row)
            file.readline()

            for i in range(self.num_cells):
                row = file.readline().strip().split()
                self.col_constraints.append(row)
        print(self.matrix)
        print(self.row_constraints)
        print(self.col_constraints)


    def get_row_constraints(self, filename):
        row_const = []
        with open(filename, 'r') as file:
            for i in range(self.num_cells):
                row = file.readline().strip().split()
                row_const.append(row)
        print(row_const)
        return row_const

    def get_col_constraints(self, filename):
        col_const = []
        with open(filename, 'r') as file:
            for i in range(self.num_cells):
                row = file.readline().strip().split()
                col_const.append(row)
        print(col_const)
        return col_const

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

    def allowed_in_row(self, val, row):
        for num in self.matrix[row]:
            if num == val:
                return False
        return True

    def allowed_in_col(self, val, col):
        for row in range(self.num_cells):
            if self.matrix[row][col] == val:
                return False
        return True

    def get_empty_cell(self):
        for row in range(self.num_cells):
            for col in range(self.num_cells):
                if not self.matrix[row][col]:
                    return (row, col)
        return False

    def solve(self, verbose=False):
        if not self.solving():
            if verbose:
                print('No solution!')
        if verbose:
            print(self.matrix)
        return self.matrix

    def solving(self):
        cell = self.get_empty_cell()
        if not cell:
            return True

        for num in range(1, self.num_cells + 2):
            if (self.allowed_in_row(num, cell[0]) and
                    self.allowed_in_col(num, cell[1]) and
                    self.satisfies_constraints(num, cell[0], cell[1])):

                self.matrix[cell[0]][cell[1]] = num
                if self.solving():
                    return True
                self.matrix[cell[0]][cell[1]] = 0

        return False


Fukoshiki("Input1.txt").solve(verbose=True)
