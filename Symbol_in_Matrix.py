n = int(input())

matrix = []

for i in range(n):
    row_data = list(input())
    matrix.append(row_data)

search_symvol = input()

position = None

for row_index in range(n):
    for cow_index in range(n):
        if matrix[row_index][cow_index] == search_symvol:
            position = (row_index, cow_index)
            print(position)
            exit()

print(f"{search_symvol} does not occur in the matrix")
