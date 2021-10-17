from TransportMatrix import TransportMatrix


class MinMethod:
    def __init__(self, transport_matrix: TransportMatrix):
        self._transport_matrix = transport_matrix
        self._a_value, self._b_value = self._transport_matrix.get_reserves()

    def start_calculation(self):
        while True:
            row, column = self._transport_matrix.get_min_free_place()
            if row == -1 and column == -1:
                return
            value1 = self._a_value[row] - self._transport_matrix.get_row_sum(row)
            value2 = self._b_value[column] - self._transport_matrix.get_column_sum(column)

            self._transport_matrix.set_value(column, row, min([value2, value1]))
