
def get_matrix (n, m, value):  #создал функцию и задал параметры
    matrix = [] # создал пустой список matrix, внутри функции get_matrix
    for i in range (n):
        matrix.append([]) #добавляем список строк
        for j in range (m):
            matrix [i].append(value) #пишем в список значения столбцов
    return (matrix)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)



