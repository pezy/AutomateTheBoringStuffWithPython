#! python3
'''TestPrintTable.py - Test print_table function'''

TABLE_DATA = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(str_list):
    '''print the table'''
    col_widths = [0] * len(str_list)
    for i in range(len(str_list)):
        for j in range(len(str_list[0])):
            if len(str_list[i][j]) > col_widths[i]:
                col_widths[i] = len(str_list[i][j])

    for j in range(len(str_list[0])):
        for i in range(len(str_list)):
            print(str_list[i][j].rjust(col_widths[i]), end=' ')
        print()

print_table(TABLE_DATA)
