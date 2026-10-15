matrix1 = [[1,2],
           [3,4]]

matrix2 = [[4,3],
           [2,1]]

matrix3 = [[4,5,6],
           [1,2,3]]

matrix4 = []

print(len(matrix3[0]))

def inspect_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    print(f"Matrix has {rows} rows and {cols} columns.")

inspect_matrix(matrix1)
inspect_matrix(matrix2)
inspect_matrix(matrix3)
inspect_matrix(matrix4)

def print_matrix(matrix):
    for row in matrix:
        print(row)

print_matrix(matrix1)
print_matrix(matrix2)
print_matrix(matrix3)
print_matrix(matrix4)

def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

# Example usage:
# result = add_matrices(matrix1, matrix2)
added_matrix = add_matrices(matrix1, matrix2)
print("Result of adding matrix1 and matrix2:")
print_matrix(added_matrix)

def dot_product(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            sum_product = 0
            for k in range(len(matrix_b)):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_product)
        result.append(row)
    return result