def sum_matrix(matrix):
    n = len(matrix)    

    first_diagonal = 0
    for i in range(n):        
        first_diagonal += matrix[i][i]

    second_diagonal = 0
    for i in range(n):        
        second_diagonal += matrix[i][n - 1 - i]

    result = first_diagonal - second_diagonal

    return first_diagonal, second_diagonal, result
    
matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 9]
]

first_diagonal, second_diagonal, result = sum_matrix(matrix)
print(f'diagonal pertama = {first_diagonal}')
print(f'diagonal kedua = {second_diagonal}')
print(f'hasil = {result}')