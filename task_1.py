import random
print('Первая матрица:\n')
matrix_1 = [[random.randint(1, 100) for x in range(10)] for i in range(10)]
for n in matrix_1: 
    print(n)

print('\nВторая матрица:\n')
matrix_2 = [[random.randint(1, 100) for x in range(10)] for i in range(10)]
for g in matrix_2:
    print(g)

print('\nСумма первой и второй матрици:\n')
summa = [[matrix_1[i][j] + matrix_2[i][j]  for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))] 
for r in summa: 
    print(r)
   


            
            
            
        
        
     



#result = [sum(i) for i in zip(matrix_1, matrix_2)] 


