class MatrixUtils:
    @staticmethod
    def matrix_print(matrix):
        for row in matrix:
            for item in row:
                print(item, end="\t")
            print()

    @staticmethod
    def column_sum(column: int, matrix) -> int:
        column_sum = 0
        for row in matrix:
            column_sum += row[column]
        return column_sum

    @staticmethod
    def column_remove(column: int, matrix):
        for row in matrix:
            row.pop(column)
