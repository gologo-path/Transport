from TransportMatrix import TransportMatrix


class PotMethod:
    _matrix = None

    def __init__(self, transport_matrix: TransportMatrix):
        self._transport_matrix = transport_matrix
        self._a_value, self._b_value = self._transport_matrix.get_reserves()

    def check_limitations(self):
        a = [None for _ in range(len(self._b_value))]
        b = [None for _ in range(len(self._a_value))]

        b[0] = 0

        again = True

        while again:
            again = False
            for row in range(len(self._transport_matrix.get_value_matrix())):
                for column in range(len(self._transport_matrix.get_value_matrix()[row])):
                    if self._transport_matrix.get_value_matrix()[row][column] != 0:
                        if a[column] is None and b[row] is None:
                            again = True
                        elif a[column] is not None and b[row] is not None:
                            pass
                        elif a[column] is not None:
                            b[row] = self._transport_matrix.get_coefficient_matrix()[row][column] - a[column]
                        else:
                            a[column] = self._transport_matrix.get_coefficient_matrix()[row][column] - b[row]

        problem = ()
        diag = [-1, -1]

        for row in range(len(self._transport_matrix.get_value_matrix())):
            for column in range(len(self._transport_matrix.get_value_matrix()[row])):
                if self._transport_matrix.get_value_matrix()[row][column] > 0:
                    if b[row] + a[column] != self._transport_matrix.get_coefficient_matrix()[row][column]:
                        problem.append((row, column))
                else:
                    if b[row] + a[column] > self._transport_matrix.get_coefficient_matrix()[row][column]:
                        problem = (row, column)

        if problem != ():
                diag = [self.find_row(problem, -1, -1), self.find_column(problem, -1, -1)]

                if diag[0] == -1 and diag[-1] == -1:
                    diag = [self.find_row(problem, 1, len(self._transport_matrix.get_value_matrix())),
                            self.find_column(problem, -1, -1)]

                if diag[0] == -1 and diag[-1] == -1:
                    diag = [self.find_row(problem, 1, len(self._transport_matrix.get_value_matrix())),
                            self.find_column(problem, 1, len(self._transport_matrix.get_value_matrix()[0]))]

                if diag[0] == -1 and diag[-1] == -1:
                    diag = [self.find_row(problem, -1, -1),
                            self.find_column(problem, 1, len(self._transport_matrix.get_value_matrix()[0]))]

        return diag, problem

    def find_row(self, point, increment, limit):
        for i in range(point[0], increment, limit):
            if self._transport_matrix.get_value_matrix()[i][point[-1]] > 0:
                return i
        return -1

    def find_column(self, point, increment, limit):
        for i in range(point[-1], increment, limit):
            if self._transport_matrix.get_value_matrix()[point[0]][i] > 0:
                return i
        return -1

    def start_calculation(self):
        while True:
            d_point, problem_point = self.check_limitations()
            if d_point != [-1, -1]:
                value = min(self._transport_matrix.get_value_matrix()[problem_point[0]][d_point[1]],
                            self._transport_matrix.get_value_matrix()[d_point[0]][problem_point[1]])

                self._transport_matrix.set_value(d_point[1], problem_point[0],
                                                 self._transport_matrix.get_value_matrix()[problem_point[0]][d_point[1]]
                                                 - value)

                self._transport_matrix.set_value(problem_point[1], d_point[0],
                                                 self._transport_matrix.get_value_matrix()[d_point[0]][problem_point[1]]
                                                 - value)

                self._transport_matrix.set_value(problem_point[1], problem_point[0],
                                                 self._transport_matrix.get_value_matrix()[problem_point[0]][problem_point[1]]
                                                 + value)

                self._transport_matrix.set_value(d_point[1], d_point[0],
                                                 self._transport_matrix.get_value_matrix()[d_point[0]][d_point[1]]
                                                 + value)
            else:
                break
