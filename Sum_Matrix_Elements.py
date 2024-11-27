row_count, col_count = [int(el) for el in input().split(", ")]

matrix = []

for row in range(row_count):

    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
    
elemnts_sum = 0

for row_data in matrix:
    elemnts_sum += sum(row_data)
    
print(elemnts_sum)
print(matrix)
