n = int(input())

matrix = []

for i in range(n):
    row_data = [int(el) for el in input().split(" ")]
    matrix.append(row_data)

diagonal_sum = 0

for row_index in range(n):
    for col_index in range(n):
        if row_index == col_index:
            diagonal_sum += matrix[row_index][col_index]

print(diagonal_sum)


