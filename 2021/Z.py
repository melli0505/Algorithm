# BOJ 1074 강다인

import sys

def z(row_s, row_e, col_s, col_e, count):
    # row_s = 행 시작, row_e = 행 끝
    # col_s = 열 시작, col_e = 열 끝
    if row_s == row and col_s == column:
        print(count)
        return

    # row와 column의 중간값으로 면을 나눔
    row_m = (row_s + row_e) // 2
    col_m = (col_s + col_e) // 2

    n = (row_m - row_s) * (col_m - col_s) # 분할된 4분면의 칸 수

    if row_s <= row < row_m and col_s <= column < col_m: # 1사분면이면
        z(row_s, row_m, col_s, col_m, count)
    elif row_s <= row < row_m and col_m <= column < col_e: # 2사분면이면
        z(row_s, row_m, col_m, col_e, n * 1 + count)
    elif row_m <= row < row_e and col_s <= column < col_m: # 3사분면이면
        z(row_m, row_e, col_s, col_m, n * 2 + count)
    else: # 4사분면이면
        z(row_m, row_e, col_m, col_e, n * 3 + count)


N, row, column = map(int, sys.stdin.readline().split())
z(0, 2**N, 0, 2**N, 0)
