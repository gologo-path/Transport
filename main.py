from TransportMatrix import TransportMatrix
from MatrixUtils import MatrixUtils
from MinMethod import MinMethod

if __name__ == '__main__':
    array = [
        [6, 1, 2, 5],
        [3, 4, 5, 2],
        [2, 4, 3, 1]
    ]

    a = [440, 180, 310]
    b = [260, 200, 340, 130]

    matrix = TransportMatrix(array, a, b)
    method = MinMethod(matrix)
    method.start_calculation()
    print(matrix.get_sum())
