values_input = input("Enter the matrix values with columns separated by commas and rows separated by semicolons: ")
power_input = int(input("Enter power of the matrix: "))

# Splitting the  elements
matrix_A = [[int(num) for num in row.split(',')] for row in values_input.split(';')]

def matrix_power(A, power):
    if power == 1:
        return A

    result = A
    for _ in range(power - 1):
        result = [[sum(result[i][k] * A[k][j] for k in range(len(A[0]))) for j in range(len(A[0]))] for i in range(len(result))]

    return result

result_matrix = matrix_power(matrix_A, power_input)

print(f"The result after raising the matrix to the power {power_input} is:")
for row in result_matrix:
    print(row)
