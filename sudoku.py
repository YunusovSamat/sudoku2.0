import numpy as np


def sudoku_print(table):
    for i in range(9):
        print('|', end='')
        for j in range(9):
            print(table[i][j], '|' if j % 3 == 2 else '', sep='', end='')
        print('\n', '-'*13+'\n' if i % 3 == 2 else '', sep='', end='')


tab_str = """\
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
tab_str = tab_str.replace('*', '0')
tab_str = tab_str.split("\n")
tab = []
for row in tab_str:
    tab.append(list(map(int, row)))

tab = np.array(tab, "int8")

sudoku_print(tab)


