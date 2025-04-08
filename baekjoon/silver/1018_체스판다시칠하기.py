import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = [[char for char in input().rstrip()] for _ in range(N)]

min_num = 64

start_W_matrix = []
start_B_matrix = []

row_type_1 = ['W','B','W','B','W','B','W','B']
row_type_2 = ['B','W','B','W','B','W','B','W']

for i in range(8):
    if i % 2 == 0:
        start_W_matrix.append(row_type_1)
        start_B_matrix.append(row_type_2)
    else:
        start_W_matrix.append(row_type_2)
        start_B_matrix.append(row_type_1)

def check_matrix_start_W(row, col):
    start_W_min_num = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if array[i][j] != start_W_matrix[i-row][j-col]:
                start_W_min_num += 1

    return start_W_min_num

def check_matrix_start_B(row, col):
    start_B_min_num = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if array[i][j] != start_B_matrix[i-row][j-col]:
                start_B_min_num += 1

    return start_B_min_num


for i in range(N - 7):
    for j in range(M - 7):
        a = check_matrix_start_W(i, j)
        b = check_matrix_start_B(i, j)
        min_num = min(min_num, a, b)



print(min_num)