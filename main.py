from TransportMatrix import TransportMatrix
from MatrixUtils import MatrixUtils
from MinMethod import MinMethod
from MainWindow import MainWindow
from PottMethod import PotMethod


if __name__ == '__main__':
    MainWindow()
#     array = [
#         [6, 1, 2, 5],
#         [3, 4, 5, 2],
#         [2, 4, 3, 1]
#     ]
#
#     a = [440, 180, 310]
#     b = [260, 200, 340, 130]
#
#     matrix = TransportMatrix(array, a, b)
#     method = MinMethod(matrix)
#     method.start_calculation()
#     MatrixUtils.matrix_print(matrix.get_value_matrix())
#     print("Z = {}".format(matrix.get_sum()))
#     pott = PotMethod(matrix)
#
#     MatrixUtils.matrix_print(matrix.get_value_matrix())
#
#     pott.start_calculation()
#
#     MatrixUtils.matrix_print(matrix.get_value_matrix())
