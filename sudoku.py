import numpy as np


class WorkSudoku:
    def __init__(self):
        self.mtx = np.array([])

    def str_to_matrix(self):
        mtx_str = """\
        9**56**2*
        6*****9**
        2*******3
        ***6***3*
        16*7*****
        ***2**7*4
        *45*****1
        *****134*
        **1**32**\
        """
        mtx_str = mtx_str.replace(' ', '')
        mtx_str = mtx_str.split("\n")
        mtx_temp = []
        for row in mtx_str:
            for elem in row:
                if elem == '*':
                    mtx_temp.append(list(range(1, 10)))
                else:
                    mtx_temp.append(int(elem))
        self.mtx = np.array(mtx_temp).reshape((9, 9))

    def insert_void_mtx_copy(self):
        mtx_temp = self.mtx.copy()
        for i, vector in enumerate(mtx_temp):
            for j, elem in enumerate(vector):
                if isinstance(elem, list):
                    mtx_temp[i, j] = []
                    for num in range(1, 10):
                        if num in elem:
                            mtx_temp[i, j].append(num)
                        else:
                            mtx_temp[i, j].append('`')
        return mtx_temp

    def print_sudoku(self):
        mtx_temp = self.insert_void_mtx_copy()
        print('-' * 36)
        for vector in mtx_temp:
            for i in range(3):
                for elem in vector:
                    if isinstance(elem, list):
                        print('{0}{1}{2}|'.format(
                            elem[0 + i * 3], elem[1 + i * 3],
                            elem[2 + i * 3]), end=""
                        )
                    else:
                        if elem:
                            if i == 1:
                                print(' {0} |'.format(elem), end='')
                            else:
                                print("   |", end='')
                        else:
                            print('{0}{0}{0}|'.format('*'), end='')
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

    def update_all_set(self):
        all_row_set = [self.get_row_set(i) for i in range(9)]
        all_col_set = [self.get_col_set(j) for j in range(9)]
        all_box_set = [self.get_box_set(i, j) for i in range(0, 8, 3)
                       for j in range(0, 8, 3)]
        for i in range(9):
            for j in range(9):
                if isinstance(self.mtx[i, j], list):
                    self.mtx[i, j] = list(set(self.mtx[i, j]) -
                                          (all_row_set[i] |
                                           all_col_set[j] |
                                           all_box_set[i // 3 * 3 + j // 3]))

    def remove_unwanted(self, i, j, removable_num):
        if isinstance(self.mtx[i, j], list):
            if removable_num in self.mtx[i, j]:
                self.mtx[i, j].remove(removable_num)

    def replace_set_with_num(self, i, j):
        self.mtx[i, j] = int(self.mtx[i, j][0])
        removable_num = self.mtx[i, j]

        for col in range(9):
            self.remove_unwanted(i, col, removable_num)
        for row in range(9):
            self.remove_unwanted(row, j, removable_num)
        for row in range(i // 3 * 3, i // 3 * 3 + 3):
            for col in range(j // 3 * 3, j // 3 * 3 + 3):
                self.remove_unwanted(row, col, removable_num)

    def search_only_value(self, i, j):
        if isinstance(self.mtx[i, j], list):
            if len(self.mtx[i, j]) == 1:
                self.replace_set_with_num(i, j)
                self.search_row(i)
                self.search_col(j)
                self.search_box(i, j)
                return True
        return False

    def search_row(self, i):
        for col in range(9):
            if self.search_only_value(i, col):
                break

    def search_col(self, j):
        for row in range(9):
            if self.search_only_value(row, j):
                break

    def search_box(self, i, j):
        for row in range(i // 3 * 3, i // 3 * 3 + 3):
            for col in range(j // 3 * 3, j // 3 * 3 + 3):
                if self.search_only_value(row, col):
                    break

    def search_all_matrix(self):
        for row in range(9):
            for col in range(9):
                self.search_only_value(row, col)

    def check_sudoku(self):
        for vector in self.mtx:
            for num in range(1, 10):
                if num not in vector:
                    return False

        for vector in self.mtx.transpose():
            for num in range(1, 10):
                if num not in vector:
                    return False

        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                for num in range(1, 10):
                    if num not in self.mtx[i: i+3, j: j+3]:
                        return False
        return True


if __name__ == '__main__':
    sudoku = WorkSudoku()
    sudoku.str_to_matrix()
    sudoku.update_all_set()
    sudoku.search_all_matrix()
    sudoku.print_sudoku()
    print(sudoku.check_sudoku())
