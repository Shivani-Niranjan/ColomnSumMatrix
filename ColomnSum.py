'''
sum of each colomn

Input
[ [1,2,3,4]
  [5,6,7,8]
  [9,2,3,4] ]

Output
[15, 10, 13, 16]
'''

row = int(input())
col = int(input())
matrix = [[int(input()) for x in range(col)] for y in range(row)]
result = []

for i in range(col):
    sum = 0
    for j in range(row):
        sum +=matrix[j][i]
    result.append(sum)

print(result)

