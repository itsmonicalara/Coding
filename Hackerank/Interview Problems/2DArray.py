import sys

def getSum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum


arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

maxSum = -63
# Double for loop, index 0 and n-1 cannot have hourglasses and first and last columns
for i in range(1, 5):
    for j in range(1, 5):
        currentSum = getSum(arr, i, j)
        if currentSum > maxSum:
            maxSum = currentSum
print(maxSum)
