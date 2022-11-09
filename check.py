import numpy as np
import filecmp

out = open("C:/Users/result_python.txt", 'w+')

for k in range(10, 101, 10):
    A = open("C:/Users/A.txt", "r")
    A1 = open("C:/Users/A1.txt", "r")
    matrix1 = np.ones((k, k), dtype=int)
    for i in range(0, k):
        for j in range(0, k):
    matrix2 = np.ones((k, k), dtype=int)
    for i in range(0, k):
        for j in range(0, k):
            matrix2[i][j] = int(A1.readline())
    mul = matrix1.dot(matrix2)
    for i in range(0, k):
        for j in range(0, k):
            out.write(str(mul[i][j]) + ' ')
        out.write('\n')
    A.close()
    A1.close()
out.close()
if filecmp.cmp('C:/Users/result_python.txt', 'C:/Users/result_C++.txt', shallow=False):
    print('Равны')
else:
    print('Неравны')
