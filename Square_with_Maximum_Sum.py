row_count, cow_count = [int(el) for el in input().split(", ")]

matrix = []

for row_index in range(row_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

max_sum = float("-inf")
sub_matrix = None

for row_index in range(row_count - 1):
    for cow_index in range(cow_count - 1):
        element = matrix[row_index][cow_index]
        next_element = matrix[row_index][cow_index + 1]
        below_element = matrix[row_index + 1][cow_index]
        element_diagonal = matrix[row_index + 1][cow_index + 1]

        sum_elements =  element + next_element + below_element + element_diagonal

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[element, next_element], [below_element, element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)



