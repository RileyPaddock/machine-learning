class Matrix:
    def __init__(self, elements=None, shape=None, fill=0):
        self.elements = elements
        if shape != None:
            self.elements = [[0 for j in range(shape[1])]
                             for i in range(shape[0])]
        else:
            self.shape = (len(elements), len(elements[0]))

        if elements == None:
            for rows in range(len(self.elements)):
                for entry in range(len(self.elements[rows])):
                    if fill == "diag":
                        self.elements[rows][rows] = 1
                    else:
                        self.elements[rows][entry] = fill

    def show(self):
        for rows in range(len(self.elements)):
            print(self.elements[rows])

    def add(input1, input2):
        result = []
        if range(len(input1.elements)) == range(len(input2.elements)):
            result = [[0 for j in range(len(input1.elements[0]))]
                      for i in range(len(input1.elements))]  #

            for i in range(len(input1.elements)):
                for j in range(len(input2.elements[0])):
                    for k in range(len(input2.elements)):
                        result[i][
                            j] = input1.elements[i][j] + input2.elements[i][j]

            return Matrix(result)

        else:

            print("Cannot add 2 matricies of different size")

    def scale(input1, scaler):
        result = []
        result = [[0 for j in range(len(input1.elements[0]))]
                  for i in range(len(input1.elements))]  #

        for i in range(len(input1.elements)):
            for j in range(len(input1.elements[0])):
                result[i][j] = scaler * input1.elements[i][j]

        return Matrix(result)

    def subtract(input1, input2):
        result = input1.add(input2.scale(-1))
        return result

    def multiply(A, B):

        if range(len(A.elements[0])) == range(len(B.elements)):

            result = Matrix(shape=(len(A.elements), len(B.elements[0])))

            for i in range(len(A.elements)):
                for j in range(len(B.elements[0])):
                    for k in range(len(B.elements)):
                        result.elements[i][
                            j] += A.elements[i][k] * B.elements[k][j]

            return result

        else:

            print("Cannot multiply A and B due to size of elements")

    def size(A):
        count = [0, 0]
        for rows in A.elements:
            count[0] += 1
        for columns in A.elements[0]:
            count[1] += 1

        return tuple(count)

    def transpose(self):
        result = Matrix(shape=(len(self.elements[0]), len(self.elements)))

        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result.elements[j][i] = self.elements[i][j]
        return result

    def exponent(A, degree):
        result = Matrix(shape=A.size(), fill='diag')
        #create identity matrix
        for x in range(degree):
            result = result.multiply(A)
        return result

    def get_pivot_row(self, column_index):
        row_count = 0
        for i in range(len(self.elements)):
            zeroes_count = 0
            if self.elements[i][column_index] != 0:
                for j in range(column_index):
                    if self.elements[i][j] == 0:
                        zeroes_count += 1
                if zeroes_count == column_index:
                    return i
            else:
                row_count += 1
        if row_count == len(self.elements):
            return None

    def swap_rows(self, row_index1, row_index2):
        row_save = []
        for i in range(len(self.elements[0])):
            row_save.append(self.elements[row_index1][i])
            self.elements[row_index1][i] = self.elements[row_index2][i]
        self.elements[row_index2] = row_save
        return self.elements

    def scale_row(self, I):
        #find first non-zero
        for i in range(len(self.elements[I])):
            if self.elements[I][i] != 0:
                zero_val = self.elements[I][i]
                break
        for i in range(len(self.elements[I])):
            self.elements[I][i] /= zero_val
        return self.elements

    def clear_below(self, I):

        pivot_as_1 = self.scale_row(I)

        for i in range(len(self.elements)):
            if i > I:
                row_first_input = self.elements[i][I]
                for j in range(len(self.elements[0])):
                    self.elements[i][j] -= row_first_input * self.elements[I][j]

        return self.elements

    def clear_above(self, I):

        pivot_as_1 = self.scale_row(I)

        for i in range(len(self.elements)):
            if i < I:
                row_first_input = self.elements[i][I]
                for j in range(len(self.elements[0])):
                    self.elements[i][j] -= row_first_input * self.elements[I][j]

        return self.elements

    def rref(self):

        if len(self.elements) >= len(self.elements[0]):
            repetitions = self.elements[0]
        else:
            repetitions = self.elements

        for i in range(len(repetitions)):
            if (self.get_pivot_row(i) == None):
                pass
            else:
                pivot1 = self.get_pivot_row(i)

            if pivot1 != i:
                self.swap_rows(i, pivot1)

            self.scale_row(i)

            self.clear_below(i)
            self.clear_above(i)

        for i in range(len(self.elements)):
            pos_self = [abs(ele) for ele in self.elements[i]]
            if sum(pos_self) == 0:
                self.swap_rows(i, len(self.elements) - 1)
                self.clear_above(len(self.elements) - 2)
            if self.elements[0][0] != 1:
                for i in range(len(self.elements)):
                    if self.elements[i][0] == 1:
                        self.swap_rows(i, 0)

        return self.elements

    def inverse(self):
        identity = Matrix(
            shape=(len(self.elements), len(self.elements[0])), fill='diag')

        if len(self.elements) == len(self.elements[0]):
            inverse = []
            saver = len(self.elements)
            for i in range(len(self.elements)):
                for j in range(len(identity.elements)):
                    self.elements[i].append(identity.elements[i][j])

            self.rref()

            for i in range(saver):
                inverse.append([])
                for j in range(saver):
                    inverse[i].append(
                        self.elements[i][len(self.elements[0]) - saver + j])

        return Matrix(inverse)

    def calc_linear_approximation_coefficients(self, data, poly_degree):
        X = Matrix(shape=(len(data), 1))
        Y = Matrix(shape=(len(data), 1))
        for i, (x, y) in enumerate(data):
            X.elements[i] = [x**i for i in range(poly_degree + 1)]
            Y.elements[i] = [y]
        x_tpose = X.transpose()
        return ((x_tpose @ X).inverse() @ (x_tpose @ Y)).elements
        #((x_tpose @ X).inverse()) @

    def __add__(self, B):
        return self.add(B)

    def __sub__(self, B):
        return self.subtract(B)

    def __mul__(self, B):
        return self.scale(B)

    def __matmul__(self, B):
        return self.multiply(B)

    def __pow__(self, B):
        return self.exponent(B)
