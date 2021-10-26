import copy
from MatrixUtils import MatrixUtils


class TransportMatrix:
    _coefficient_matrix = None
    _value_matrix = None
    _a_values = None
    _b_values = None

    def __init__(self, matrix: list, a_values: list, b_values: list):
        if len(a_values) != len(matrix) or len(b_values) != len(matrix[0]):
            raise ValueError("TransportMatrix: The lengths of the columns and rows of the matrix do not match the"
                             " lengths of a_values or b_values")

        self._coefficient_matrix = copy.deepcopy(matrix)
        self._value_matrix = [[0 for _ in range(len(self._coefficient_matrix[0]))]
                              for _ in range(len(self._coefficient_matrix))]

        self._a_values = a_values.copy()
        self._b_values = b_values.copy()

    def get_value_matrix(self):
        return self._value_matrix

    def get_coefficient_matrix(self):
        return self._coefficient_matrix

    def get_column_sum(self, column) -> int:
        return MatrixUtils.column_sum(column, self._value_matrix)

    def get_row_sum(self, row) -> int:
        return sum(self._value_matrix[row])

    def set_value(self, column, row, value):
        if value < 0:
            raise ValueError("TransportMatrix: value < 0")
        if not self._validate_value(column, row, value):
            raise ValueError("TransportMatrix: too big value")
        else:
            self._value_matrix[row][column] = value

    def get_sum(self) -> int:
        summ = 0

        for row in range(len(self._value_matrix)):
            for column in range(len(self._value_matrix[0])):
                summ += self._value_matrix[row][column] * self._coefficient_matrix[row][column]

        return summ

    def get_reserves(self):
        return self._a_values, self._b_values

    def get_min_free_place(self) -> tuple:
        coefficients = copy.deepcopy(self._coefficient_matrix)

        while True:
            mins = [min(row) for row in coefficients]
            min_value = min(mins)
            if min_value == 10 ** 18:
                return -1, -1
            row = mins.index(min_value)
            column = coefficients[row].index(min_value)

            if self._value_matrix[row][column] > 0 or sum(self._value_matrix[row]) >= self._a_values[row] \
                    or MatrixUtils.column_sum(column, self._value_matrix) >= self._b_values[column]:
                coefficients[row][column] = 10 ** 18
            else:
                return row, column

    def _validate_value(self, column: int, row: int, value: int) -> bool:
        return MatrixUtils.column_sum(column, self._value_matrix) - self._value_matrix[row][column] + value <= \
               self._b_values[column] and sum(self._value_matrix[row]) - self._value_matrix[row][column] + value \
               <= self._a_values[row]
