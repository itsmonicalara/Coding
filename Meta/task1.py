def solution(numbers):
    new_array = []
    for i in range(1, len(numbers) - 1):
        # if number is bigger than the previous 2 numbers
        if numbers[i] > numbers[i - 2] and numbers[i] > numbers[i - 1]:
            numbers[i] = numbers[i]
        else:
            numbers[i] = 0
    return numbers

# Read array in a single line
numbers = [int(i) for i in input().split()]
# [2, 1, 3, 3]

print(solution(numbers)) 