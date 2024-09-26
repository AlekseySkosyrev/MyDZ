def get_code(stone):
    code = ''
    for i in range(1, stone):
        for j in range(2, stone):
            if j <= i:
                continue
            if stone % (i + j) == 0:
                code += str(i) + str(j)
    return code
n = int(input('Что на первом камне? (целое число от 3 до 20) '))
result = get_code(n)
print('Нацарапайте на другом камне:', result)