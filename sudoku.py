import numpy as np


class WorkSudoku:
    def __init__(self):
        self.mtx = []

    def str_to_mtx(self):
        mtx_str = """\
        ***6**1*7
        68*9513**
        **3**2568
        *4*81**2*
        ******85*
        *9**65*73
        4*9**3*85
        162**9*3*
        5**7*6***\
        """
        mtx_str = mtx_str.replace(' ', '')
        mtx_str = mtx_str.split("\n")

        for row in mtx_str:
            for elem in row:
                if elem == '*':
                    self.mtx.append(list(range(1, 10)))
                else:
                    self.mtx.append(int(elem))
        self.mtx = np.array(self.mtx).reshape((9, 9))

    def print_sudoku(self):
        print('-' * 36)
        for vector in self.mtx:
            for i in range(3):
                for elem in vector:
                    if isinstance(elem, list):
                        print(elem[0 + i * 3], elem[1 + i * 3], elem[2 + i * 3], '|', sep='', end='')
                    else:
                        if i % 3 == 1:
                            print(' ', elem, ' |', sep='', end='')
                        else:
                            print('   |', sep='', end='')
                print()
            print('-' * 36)
        print()

    def get_row_set(self, i):
        set_temp = set()
        for elem in self.mtx[i]:
            if isinstance(elem, int):
                set_temp.add(elem)
        return set_temp

    def get_col_set(self, j):
        set_temp = set()
        for elem in self.mtx[:, j]:
            if isinstance(elem, int):
                set_temp.add(elem)
        return set_temp

    def get_box_set(self, i, j):
        set_temp = set()
        row_bgn = i // 3 * 3
        row_end = (i // 3 + 1) * 3
        col_bgn = j // 3 * 3
        col_end = (j // 3 + 1) * 3
        for elem in self.mtx[row_bgn: row_end, col_bgn: col_end].ravel():
            if isinstance(elem, int):
                set_temp.add(elem)
        return set_temp

    def get_all_set(self, i, j):
        return (set(range(1, 10)) - (self.get_row_set(i) |
                self.get_col_set(j) | self.get_box_set(i, j)))


if __name__ == '__main__':
    sudoku = WorkSudoku()
    sudoku.str_to_mtx()
    # sudoku.print_sudoku()
    print(sudoku.get_all_set(0, 8))



