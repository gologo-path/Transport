from WindowPattern import WindowPattern
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from TransportMatrix import TransportMatrix
from MinMethod import MinMethod
from MatrixUtils import MatrixUtils
from PottMethod import PotMethod


class MainWindow(WindowPattern):
    rows = 0
    columns = 0

    a_values = []
    b_values = []

    matrix = []

    def __init__(self):
        super().__init__("Transport")

    def _new_command(self):
        super()._clean_frame()

        self.dialog_window = tk.Tk()
        self.dialog_window.geometry("300x100")
        self.dialog_window.resizable(False, False)
        label = tk.Label(self.dialog_window, text="Введите длинну и высоту матрицы, "
                                                  "но не больше 10",
                         font=("Times new Roman", 10))
        label.pack()
        self.spinbox_a = tk.Spinbox(self.dialog_window, from_=2, to=10, width=7, font="10")
        self.spinbox_b = tk.Spinbox(self.dialog_window, from_=2, to=10, width=7, font="10")
        self.spinbox_a.bind('<Return>', self._set_number_var)
        self.spinbox_b.bind('<Return>', self._set_number_var)
        self.spinbox_a.pack()
        self.spinbox_b.pack()
        button = tk.Button(self.dialog_window, text="Ввод", command=self._set_number_var, font="10")
        button.pack()

    def _set_number_var(self):
        inp_str_a = self.spinbox_a.get()
        inp_str_b = self.spinbox_b.get()

        if not inp_str_a.isdigit() or not inp_str_b.isdigit():
            messagebox.showerror("Ошибка", "Ожидается ввод числа")
        else:
            self.rows = int(inp_str_a)
            self.columns = int(inp_str_b)
            self.dialog_window.destroy()
            self._build_matrix()

    def _build_matrix(self):
        self._matrix = [[None for _ in range(0, self.columns)] for _ in range(0, self.rows)]
        self._a_values = [None for _ in range(self.rows)]
        self._b_values = [None for _ in range(self.columns)]

        for y in range(0, self.rows):
            self._a_values[y] = tk.StringVar()
            tmp = tk.Entry(textvariable=self._a_values[y], width=10)
            tmp.grid(row=y + 1, column=0, padx=15, pady=5)
            super()._destroy_objects.append(tmp)

            for x in range(0, self.columns):
                self._b_values[x] = tk.StringVar()
                tmp = tk.Entry(textvariable=self._b_values[x], width=10)
                tmp.grid(row=0, column=x + 1, padx=5, pady=15)
                super()._destroy_objects.append(tmp)

                self._matrix[y][x] = tk.StringVar()
                tmp = tk.Entry(textvariable=self._matrix[y][x], width=10)
                tmp.grid(row=y + 1, column=x + 1, padx=5, pady=5)
                super()._destroy_objects.append(tmp)

            # super()._destroy_objects.append(tmp)

        tmp = tk.Button(text="Расчет", command=self._validate_data, width=20)
        tmp.grid(row=self.rows + 5, columnspan=self.columns + 5)
        super()._destroy_objects.append(tmp)

    def _start_calculations(self):
        trm = TransportMatrix(self.matrix, self.a_values, self.b_values)
        method = MinMethod(trm)
        method.start_calculation()

        super()._clean_frame()

        row, column = self._build_label_matrix(trm, 0, 0, "Min method:")

        method = PotMethod(trm)
        method.start_calculation()

        self._build_label_matrix(trm, row+2, 0, "Coeff method:")

    def _validate_data(self):
        self.matrix = [[None for _ in range(0, self.columns)] for _ in range(0, self.rows)]
        for item in self._a_values:
            try:
                tmp = int(item.get())
            except ValueError:
                return
            self.a_values.append(tmp)

        for item in self._b_values:
            try:
                tmp = int(item.get())
            except ValueError:
                return
            self.b_values.append(tmp)

        for row in range(len(self._matrix)):
            for column in range(len(self._matrix[row])):
                try:
                    tmp = int(self._matrix[row][column].get())
                except ValueError:
                    return
                self.matrix[row][column] = tmp

        self._start_calculations()

    def _build_label_matrix(self, trm: TransportMatrix, row, column, message: str):
        a, b = trm.get_reserves()
        y = x = 0

        tmp = tk.Label(text=message)
        tmp.grid(row=y + 1 + row, column=0 + column, padx=15, pady=15)
        super()._destroy_objects.append(tmp)

        row += 1
        tmp.grid(row=y + 1 + row, column=0 + column, padx=15, pady=5)
        super()._destroy_objects.append(tmp)

        for y in range(0, len(trm.get_value_matrix())):
            tmp = tk.Label(text=str(a[y]), width=10)
            tmp.grid(row=y + 1 + row, column=0 + column, padx=15, pady=5)
            super()._destroy_objects.append(tmp)

            for x in range(0, len(trm.get_value_matrix()[y])):
                tmp = tk.Label(text=str(b[x]), width=10)
                tmp.grid(row=0 + row, column=x + 1 + column, padx=5, pady=15)
                super()._destroy_objects.append(tmp)

                tmp = tk.Label(text=str(trm.get_value_matrix()[y][x]), width=10)
                tmp.grid(row=y + 1 + row, column=x + 1 + column, padx=5, pady=5)
                super()._destroy_objects.append(tmp)

        row += 1

        tmp = tk.Label(text="Z = {}".format(str(trm.get_sum())))
        tmp.grid(row=y + 1 + row, column=x + 1 + column, padx=5, pady=5)
        super()._destroy_objects.append(tmp)

        return y+2, x