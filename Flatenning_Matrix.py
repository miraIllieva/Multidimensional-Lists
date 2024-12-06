n = int(input())

matrix = []

for i in range(n):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

print(matrix)
